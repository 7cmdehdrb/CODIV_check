from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages

# Create your views here.


class HomeView(View):
    def get(self, request):
        # messages.add_message(request, messages.INFO, "테스트!")
        return render(request, "home.html")
