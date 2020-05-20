from django.urls import path
from . import views as organization_view

app_name = "organization"

urlpatterns = [
    path("menu/", organization_view.OrganizationMenuView.as_view(), name="menu"),
    path("new/", organization_view.OrganizationView.as_view(), name="neworganization"),
]
