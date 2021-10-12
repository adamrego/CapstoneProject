from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.views import View
from Classes.functions import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate




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


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})
