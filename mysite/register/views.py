from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.
def home(response):
    if response.method=="GET":
        if User.is_active:
            return redirect("/")
        else:
            return redirect("/login")



def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = RegisterForm()

    return render(response, "register/register.html", {"form":form})