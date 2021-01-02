from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        form = RegisterForm(request.POST)
        return render(request, 'signup.html',{'form':form})



def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("index")
    else:
        form = AuthenticationForm(request.POST)
        return render(request,'login.html',{'form':form})
def logout_views(request):
    if request.method == "POST":
        logout(request)

    return redirect('index')