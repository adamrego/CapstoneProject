from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render
from django.views import View
from django.contrib import messages

from CapstoneProject.forms import NewUserForm
from Classes.functions import *


class Home(View):
    def get(self, request):
        form = NewUserForm()
        log = AuthenticationForm()
        return render(request, "home.html", context={"register_form": form, "login_form": log})


def redirect_home(request):
    form = NewUserForm()
    log = AuthenticationForm()
    return render(request, "home.html", context={"register_form": form, "login_form": log})

def redirect_profile(request):
    form = NewUserForm()
    log = AuthenticationForm()
    return render(request, "editProfile.html", context={"register_form": form, "login_form": log})


def redirect_about(request):
    form = NewUserForm()
    log = AuthenticationForm()
    return render(request, "about.html", context={"register_form": form, "login_form": log})


def redirect_pools(request):
    form = NewUserForm()
    log = AuthenticationForm()
    return render(request, "pools.html", context={"register_form": form, "login_form": log})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "home.html")
    form = NewUserForm()
    log = AuthenticationForm()
    return render(request=request, template_name="home.html", context={"register_form": form, "login_form": log})


def login_request(request):
    if request.method == "POST":
        log = AuthenticationForm(request, data=request.POST)
        if log.is_valid():
            username = log.cleaned_data.get('username')
            password = log.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                form = NewUserForm()
                messages.info(request, "You are now logged in as {username}.")
                return render(request, "home.html", context={"register_form": form, "login_form": log})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = NewUserForm()
    log = AuthenticationForm()
    return render(request=request, template_name="home.html", context={"register_form": form, "login_form": log})
