from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accaunts.forms import RegisterForm, LoginForm


# from page.models import CustomUser


def register_part(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            p=form.cleaned_data['password']
            user.set_password(p)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accaunts/register.html', {'form':form})


def login_part(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request, user )
                return redirect('objects')
            else:
                form.add_error(None, 'incorrect password or username')

    else:
        form = LoginForm()
    return render(request, 'accaunts/login.html', {'form':form})


def logout_part(request):
    logout(request)
    return redirect('login')


