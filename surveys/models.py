from django.db import models
from core import models as core_model
from datetime import datetime
from django.utils.dateformat import DateFormat

# Create your models here.


class Survey(core_model.TimeStampedModel):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user"
    )
    date = models.DateField(default=DateFormat(datetime.now()).format("Y-m-d"))
    question1 = models.BooleanField(default=False)
    question2 = models.BooleanField(default=False)
    question3 = models.BooleanField(default=False)
    question4 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + " : " + self.user.username
