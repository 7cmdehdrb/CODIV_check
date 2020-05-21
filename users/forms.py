from django import forms
from organizations import models as organization_model
from . import models


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User

        fields = (
            "email",
            "nickname",
            "password",
            "re_password",
            "gender",
            "age",
            "job",
        )

        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "email@naver.com"}),
            "nickname": forms.TextInput(attrs={"placeholder": "홍길동"}),
        }

        labels = {
            "email": "이메일",
            "nickname": "이름",
            "password": "비밀번호",
            "re_password": "비밀번호 확인",
            "gender": "성별",
            "age": "나이",
            "job": "직업",
        }

    password = forms.CharField(widget=forms.PasswordInput(), label="비밀번호")
    re_password = forms.CharField(widget=forms.PasswordInput(), label="비밀번호 확인")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 가입한 사용자압니다", code="existing_user")
        except models.User.DoesNotExist:
            return email

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("패스워드가 일치하지 않습니다")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "이메일"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 다릅니다"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("해당 유저가 존재하지 않습니다"))


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.User

        fields = ("desired_organization",)

        widgets = {
            "desired_organization": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(OrganizationForm, self).__init__(*args, **kwargs)
        self.fields[
            "desired_organization"
        ].queryset = organization_model.Organization.objects.filter(isrecruited=True)

    def save(self, *args, **kwargs):
        user = super().save()
        user.save()
