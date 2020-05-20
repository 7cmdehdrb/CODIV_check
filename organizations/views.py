from django.shortcuts import render
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.views.generic import View, FormView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from . import forms, models

# Create your views here.


class OrganizationMenuView(View):
    def get(self, request):
        return render(request, "organizations/organizationMenu.html")


class OrganizationView(FormView):

    template_name = "organizations/newOrganization.html"
    form_class = forms.OrganizationForm

    def get_success_url(self):
        return reverse_lazy("core:core")

    def get_initial(self):
        initial = super().get_initial()
        initial["master"] = self.request.user
        return initial

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
