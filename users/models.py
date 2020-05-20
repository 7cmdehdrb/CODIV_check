from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from emails import sendVerifyEmail
from core import models as core_model

# Create your models here.


class AbstractItem(core_model.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Job(AbstractItem):

    """ Job Model Definition """

    class Meta:
        verbose_name = "Job"


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(
        default=15, validators=[MinValueValidator(15), MaxValueValidator(99)]
    )
    gender = models.CharField(choices=GENDER_CHOICE, default=GENDER_MALE, max_length=6)
    job = models.ForeignKey(
        "Job", related_name="job", on_delete=models.CASCADE, null=True
    )
    desired_organization = models.ManyToManyField(
        "organizations.Organization", related_name="desired_organization", blank=True
    )

    email_secret = models.CharField(max_length=20, default=uuid.uuid4().hex[:20])
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def verify_email(self):
        if self.email_verified is False:
            sendVerifyEmail(self.email, self.email_secret)
            self.save()
        return
