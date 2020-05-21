from django.urls import path
from . import views as organization_view

app_name = "organization"

urlpatterns = [
    path("menu/", organization_view.OrganizationMenuView.as_view(), name="menu"),
    path("new/", organization_view.OrganizationView.as_view(), name="neworganization"),
    path(
        "update-organization/<int:pk>/",
        organization_view.OrganizationUpdateView.as_view(),
        name="updateorganization",
    ),
    path("error/", organization_view.OrganizationUnvalidView.as_view(), name="unvalid"),
]
