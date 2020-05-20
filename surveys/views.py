from django.shortcuts import render, reverse
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.views.generic import FormView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from . import forms, models
from organizations import models as organization_model
from users import models as user_model
from users import mixins

# Create your views here.


class SurveyView(mixins.LoggedInOnlyView, FormView):

    template_name = "surveys/newSurvey.html"
    form_class = forms.SurveyForm

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = self.get_context_data(**kwargs)
        context["todate"] = DateFormat(datetime.now()).format("Y-m-d")
        return self.render_to_response(context)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:core")

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        initial["date"] = DateFormat(datetime.now()).format("Y-m-d")
        return initial

    def form_valid(self, form):

        moral = form.cleaned_data.get("question4")

        survey = models.Survey.objects.filter(
            date=DateFormat(datetime.now()).format("Y-m-d")
        ).filter(user=self.request.user)

        if moral:

            if len(survey) == 0:
                messages.add_message(self.request, messages.INFO, "감사합니다!")
                form.save()

            else:
                messages.add_message(self.request, messages.ERROR, "오늘은 이미 참여하였습니다")

        else:
            messages.add_message(self.request, messages.ERROR, "당신의 양심은 안녕하십니까?")

        return super().form_valid(form)


class SurveyListView(mixins.LoggedInOnlyView, mixins.MasterUserOnlyView, ListView):
    def get(self, request):

        result = []

        organizaion = organization_model.Organization.objects.filter(
            master__username=self.request.user
        ).values("users__username", "users__nickname")

        for o in organizaion:

            survey = models.Survey.objects.filter(
                user__username=o["users__username"],
                date=DateFormat(datetime.now()).format("Y-m-d"),
            )

            if len(survey) == 1:
                result.append(survey[0])

            else:
                temp = {"user": o["users__nickname"], "option": True}
                result.append(temp)

        return render(request, "surveys/surveylist.html", {"surveys": result},)
