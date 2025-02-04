# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Views that require login
@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def services(request):
    return render(request, 'services.html')

@login_required(login_url='/login/')
def solutions(request):
    return render(request, 'solutions.html')

@login_required(login_url='/login/')
def clients(request):
    return render(request, 'clients.html')

@login_required(login_url='/login/')
def partners(request):
    return render(request, 'partners.html')

@login_required(login_url='/login/')
def gallery(request):
    return render(request, 'gallery.html')


# Registration View
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully! You can log in now.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'register.html')

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

