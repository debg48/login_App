from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Signin test app !")

def signup(request):
    return render(request,"auth/signup.html")

def signin(request):
    return render(request,"auth/signin.html")

def signout(request):
    pass