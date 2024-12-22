from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import User

# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create(
            full_name=full_name,
            username=username,
            password=password,
        )
        user.save()
        return redirect("index")
    context = {}
    return render(request, "register.html", context)


def main1(request):
    context = {}
    return render(request, "main1.html", context)


def main2(request):
    context = {}
    return render(request, "main2.html", context)


def main3(request):
    context = {}
    return render(request, "main3.html", context)


def main4(request):
    context = {}
    return render(request, "main4.html", context)


def main5(request):
    context = {}
    return render(request, "main5.html", context)


def main6(request):
    context = {}
    return render(request, "main6.html", context)


def main7(request):
    context = {}
    return render(request, "main7.html", context)
