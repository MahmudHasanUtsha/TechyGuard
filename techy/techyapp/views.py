# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# ✅ All pages are now public (no login required)
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def email_services(request):
    return render(request, 'email_services.html')
def domain_hosting(request):
    return render(request, 'domain_hosting.html')
def website_creation(request):
    return render(request, 'website_creation.html')
def software_development(request):
    return render(request, 'software_development.html')
def hardware_purchase(request):
    return render(request, 'hardware_purchase.html')
def security_solutions(request):
    return render(request, 'security_solutions.html')

def solutions(request):
    return render(request, 'solutions.html')

def clients(request):
    return render(request, 'clients.html')

def partners(request):
    return render(request, 'partners.html')

def gallery(request):
    return render(request, 'gallery.html')

# ✅ Registration View
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

# ✅ Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('index')  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

# ✅ Logout View (Redirect to home after logout)
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')  # Redirect to home page after logout
