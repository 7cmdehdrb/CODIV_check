from django.shortcuts import render, reverse
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.views.generic import View, FormView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from . import forms, models
from users import mixins

# Create your views here.


class OrganizationMenuView(mixins.LoggedInOnlyView, View):
    def get(self, request):
        return render(request, "organizations/organizationMenu.html")


class OrganizationView(
    mixins.LoginRequiredMixin, mixins.VerifiedUserOnlyView, FormView
):

    template_name = "organizations/newOrganization.html"
    form_class = forms.OrganizationForm

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse_lazy("organization:menu")

    def get_initial(self):
        initial = super().get_initial()
        initial["master"] = self.request.user
        initial["users"] = self.request.user
        return initial

    def form_valid(self, form):

        organization = models.Organization.objects.filter(
            master__username=self.request.user.username
        )

        if len(organization) != 0:
            print("??")
            messages.add_message(self.request, messages.ERROR, "그룹 생성은 1회로 제한됩니다")

        else:
            form.save()
            messages.add_message(self.request, messages.INFO, "성공적으로 그룹을 만들었습니다!")

        return super().form_valid(form)
