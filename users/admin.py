from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.Job)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name",)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "nickname",
                    "age",
                    "gender",
                    "job",
                    "desired_organization",
                    "email_secret",
                    "email_verified",
                )
            },
        ),
    )

    list_display = ("nickname", "age", "gender", "email", "job", "email_verified")

    list_filter = (
        "gender",
        "is_superuser",
    )

    filter_horizontal = ("desired_organization",)

    search_fields = ("nickname", "email", "job__name")
