from django import forms
from . import models


class SurveyForm(forms.ModelForm):
    class Meta:
        model = models.Survey
        fields = (
            "user",
            "date",
            "question1",
            "question2",
            "question3",
            "question4",
        )
        widgets = {
            "user": forms.HiddenInput(),
            "date": forms.HiddenInput(),
        }

        labels = {
            "question1": "이태원 클럽 다녀옴?",
            "question2": "해외 다녀왔음?",
            "question3": "기침 등 증상 있음?",
            "question4": "양심 있음?",
        }

    def save(self, *args, **kwargs):
        survey = super().save()
        survey.save()
