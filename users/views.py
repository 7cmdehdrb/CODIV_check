from django.shortcuts import redirect, reverse, render
from django.contrib.auth import login, logout, authenticate
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms, models, mixins


# Create your views here.


class SignUpView(mixins.LoggedOutOnlyView, FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            user.verify_email()
            messages.add_message(self.request, messages.INFO, "회원가입 완료!\n이메일 인증을 해주세요")
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:core")


class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.INFO, "환영합니다")
        else:
            messages.add_message(self.request, messages.ERROR, "로그인 실패")
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        print(next_arg)
        if next_arg is not None:
            return next_arg
        else:
            return reverse_lazy("core:core")


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "안녕히가세요")
    return redirect(reverse("core:core"))


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        messages.add_message(request, messages.INFO, "인증을 완료하셨습니다!")
    except models.User.DoesNotExist:
        messages.add_message(request, messages.ERROR, "인증을 완료할 수 없습니다")
        pass
    return redirect(reverse("core:core"))


class UserProfileView(mixins.LoggedInOnlyView, DetailView):

    model = models.User
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
