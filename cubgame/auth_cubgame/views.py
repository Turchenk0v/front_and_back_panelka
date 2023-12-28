from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm


def register(request):
    error = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.data.get("username"))
            except ObjectDoesNotExist:
                user = None
            if form.data.get("password") == form.data.get("check_password") and user is None:
                user = User.objects.create(username=form.data.get("username"))
                user.set_password(form.data.get("password"))
                user.save()
                user = authenticate(username=form.data.get("username"), password=form.data.get("password"))
                login(request, user)
                return redirect("home")
            else:
                error = f"Такой пользователь уже существует или неправильный пароль."
    else:
        form = RegisterForm()
    data = {"form": form, "error": error}
    return render(request, "auth/register.html", data)


def logout_for_cubgame(request):
    logout(request)
    return redirect("home")


def login_for_cubgame(request):
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.data.get("username"))
            except ObjectDoesNotExist:
                user = None
            if user is not None:
                if user.check_password(form.data.get("password")):
                    user = authenticate(username=form.data.get("username"), password=form.data.get("password"))
                    login(request, user)
                    return redirect("home")
            else:
                error = "Проверьте username/password."
    else:
        form = LoginForm()
    data = {"form": form, "error": error}
    return render(request, "auth/login.html", data)
