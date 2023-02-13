from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"auth/index.html")

def signup(request):

    if request.method == 'POST':

        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm')

        user = User.objects.create_user(username,email,pass1)

        user.first_name = fname
        user.LAst_name = lname

        user.save()

        messages.success(request,"Account Created Successsfully !")
        return redirect('signin')

    return render(request,"auth/signup.html")

def signin(request):
    return render(request,"auth/signin.html")

def signout(request):
    pass