from django.contrib import admin
from . import models
from organizations import models as organization_model

# Register your models here.


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Infomations", {"fields": ("user", "date",)},),
        (
            "Questions",
            {"fields": ("question1", "question2", "question3", "question4",)},
        ),
    )

    list_display = (
        "user",
        "date",
        "question1",
        "question2",
        "question3",
        "question4",
    )

    list_filter = (
        "user__desired_organization",
        "question1",
        "question2",
        "question3",
        "question4",
        "date",
    )

    search_fields = ("user__username",)
