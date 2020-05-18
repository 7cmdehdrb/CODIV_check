from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("avatar", "age", "gender", "job", "organization",)},
        ),
    )

    list_display = ("username", "age", "gender", "email", "is_superuser")
