from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/signup.html", {"form": form})
