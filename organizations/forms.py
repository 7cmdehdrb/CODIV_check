from django import forms
from users import models as user_model
from . import models


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ("name", "master", "location", "phone", "users", "isrecruited")
        widgets = {
            "master": forms.HiddenInput(),
            "isrecruited": forms.HiddenInput(),
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


class OrganizationUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = (
            "master",
            "name",
            "location",
            "phone",
            "isrecruited",
            "users",
        )
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "주식회사 OOOO"}),
            "location": forms.TextInput(attrs={"placeholder": "서울특별시 강남구"}),
            "users": forms.CheckboxSelectMultiple(),
        }
        labels = {
            "name": "그룹이름",
            "location": "주소",
            "phone": "대표전화",
        }

    def __init__(self, *args, **kwargs):
        super(OrganizationUpdateForm, self).__init__(*args, **kwargs)
        self.fields["users"].queryset = user_model.User.objects.filter(
            desired_organization__name=self["name"].value()
        )

    def get_initial(self):
        initial = super().get_initial()
        initial["master"] = self.request.user
        return initial

    def save(self, *args, **kwargs):
        organization = super().save()
        organization.save()
