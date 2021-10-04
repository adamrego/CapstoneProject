from django.shortcuts import render, redirect
from django.views import View
from Classes.functions import *


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

