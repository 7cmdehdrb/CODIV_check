from django.urls import path
from . import views as user_view

app_name = "user"

urlpatterns = [
    path("signup/", user_view.SignUpView.as_view(), name="signup"),
    path("login/", user_view.LoginView.as_view(), name="login"),
    path("logout/", user_view.logout_view, name="logout"),
    path(
        "verify/<str:key>/",
        user_view.complete_verification,
        name="complete_verification",
    ),
]
