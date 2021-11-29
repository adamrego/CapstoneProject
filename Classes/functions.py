from django.contrib.auth.models import User
from django.shortcuts import redirect

from CapstoneProject.models import *

from pprint import pprint


def editAccount(username="", password="", email=""):
    # precodition user must exist
    # post condition the users account information as been updated

    User.objects.filter(username=username).update(password=password, email=email)
    return ""
