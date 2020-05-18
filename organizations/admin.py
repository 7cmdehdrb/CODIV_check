from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Infomations", {"fields": ("name", "master", "location", "phone", "users")}),
    )

    list_display = (
        "name",
        "master",
        "location",
        "phone",
    )

    filter_horizontal = ("users",)
