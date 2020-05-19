from django.shortcuts import render
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from . import forms, models

# Create your views here.


class SurveyView(FormView):

    template_name = "surveys/newSurvey.html"
    form_class = forms.SurveyForm

    def get_success_url(self):
        # next_arg = self.request.GET.get("next")
        # if next_arg is not None:
        #     return next_arg
        # else:
        #     return reverse_lazy("core:core")
        return reverse("core:core")

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        initial["data"] = DateFormat(datetime.now()).format("Y-m-d")
        return initial

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
