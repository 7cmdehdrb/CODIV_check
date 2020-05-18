from django.shortcuts import redirect, reverse, render
from django.contrib.auth import login, logout, authenticate
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms, models


# Create your views here.


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        # Put function here
        return reverse_lazy("core:core")
