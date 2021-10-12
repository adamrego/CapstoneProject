from django.shortcuts import render, redirect
from django.views import View
from Classes.functions import *


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})


def redirect_home(request):
    response = redirect('/Home/')
    return render(request, "home.html")


def redirect_about(request):
    response = redirect('/about/')
    return render(request, "about.html")


def redirect_lanes(request):
    response = redirect('/lanes/')
    return render(request, "lanes.html")

def redirect_pools(request):
    response = redirect('/pools/')
    return render(request, "pools.html")