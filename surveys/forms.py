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
            "question1": "최근에 이태원에 다녀온적이 있나요?",
            "question2": "최근에 해외에 다녀온적이 있나요?",
            "question3": "최근에 기침 등의 증상이 있나요?",
            "question4": "성실하게 답변하였나요?",
        }

    def save(self, *args, **kwargs):
        survey = super().save()
        survey.save()
