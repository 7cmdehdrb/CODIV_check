from django.urls import path
from . import views as survey_view

app_name = "survey"

urlpatterns = [
    path("new/", survey_view.SurveyView.as_view(), name="newsurvey"),
    path("list/", survey_view.SurveyListView.as_view(), name="list"),
    path("confirm/", survey_view.SurveyConfirmView.as_view(), name="confirm"),
]
