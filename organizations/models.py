from django.db import models
from core import models as core_model
from phone_field import PhoneField

# Create your models here.


class Organization(core_model.TimeStampedModel):

    name = models.CharField(max_length=20)
    master = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="master"
    )
    location = models.CharField(max_length=300)
    phone = PhoneField(blank=True, help_text="Contact phone number")
    users = models.ManyToManyField("users.User", related_name="users")

    def __str__(self):
        return self.name
