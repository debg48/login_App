from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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

    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"auth/index.html",{ "fname": fname })
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")      

    return render(request,"auth/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect("home")