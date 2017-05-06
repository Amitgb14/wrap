
import os
import shutil

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.utils import timezone
from django.utils.safestring import mark_safe

from dashboard.forms import UserLoginForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "sign-in.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")

