from django import forms
from . import models


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ("name", "master", "location", "phone", "users")
        widgets = {
            "master": forms.HiddenInput(),
            "name": forms.TextInput(attrs={"placeholder": "주식회사 OOOO"}),
            "location": forms.TextInput(attrs={"placeholder": "서울특별시 강남구"}),
        }
        labels = {
            "name": "그룹이름",
            "location": "주소",
            "phone": "대표전화",
        }

    def save(self, *args, **kwargs):
        organization = super().save()
        organization.save()
