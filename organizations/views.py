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

        result = None

        organization = models.Organization.objects.filter(
            master=self.request.user
        ).values("pk")

        if len(organization) != 0:
            result = organization[0]["pk"]

        return render(
            request, "organizations/organizationMenu.html", {"organizationpk": result},
        )


class OrganizationUnvalidView(View):
    def get(self, request):
        messages.add_message(self.request, messages.ERROR, "잘못된 접근입니다!")

        result = None

        organization = models.Organization.objects.filter(
            master=self.request.user
        ).values("pk")

        if len(organization) != 0:
            result = organization[0]["pk"]

        return render(
            request, "organizations/organizationMenu.html", {"organizationpk": result},
        )


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
            messages.add_message(self.request, messages.ERROR, "그룹 생성은 1회로 제한됩니다")

        else:
            form.save()
            messages.add_message(self.request, messages.INFO, "성공적으로 그룹을 만들었습니다!")

        return super().form_valid(form)


class OrganizationUpdateView(
    mixins.LoggedInOnlyView, mixins.VerifiedUserOnlyView, UpdateView
):
    model = models.Organization
    template_name = "organizations/update-organization.html"
    form_class = forms.OrganizationUpdateForm

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "수정 완료!")
        return reverse_lazy("organization:menu")
