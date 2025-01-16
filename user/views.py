from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('game:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('user:login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('game:dashboard') 
            else:
                return render(request, 'user/login.html', {'form': form, 'invalid_creds': True})
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'game/dashboard.html') 
