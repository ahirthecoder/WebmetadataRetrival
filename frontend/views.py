from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import Group
from .models import extenduser


def home(request):

    return render(request, 'user/home.html', )

# About Page


def documentation(request):
    return render(request, 'user/documentation.html')
# contact


def contact(request):
    return render(request, 'user/contact.html')
# Dashboard


def dashboard(request,):
    if request.user.is_authenticated:

        user = request.user
        data = extenduser.objects.filter(user=request.user)
        return render(request, 'user/dashboard.html', {'user': data})
    else:
        return HttpResponseRedirect('/login/')

# Logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

# Sign up


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'congratulatons your Account is created Now login with your creditentials')

            user = form.save()
            #group = Group.objects.get(name='Author')
            #user.groups.add(group)

    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Succefully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')
