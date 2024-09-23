from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str


# Home page view
def index(request):
    return render(request, 'index.html')


# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        # Authenticate the user
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            # Log the user in
            auth_login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('chat')  # Redirect to the 'chat' page after login
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')  # Stay on the login page if credentials are incorrect

    return render(request, 'login.html')


# Signup view
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for existing username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Please try another username.")
            return redirect('signup')

        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Validate username length
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters!")
            return redirect('signup')

        # Validate matching passwords
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if username is alphanumeric
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('signup')

        # Create the user and save
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()

        # Success message and redirect to login
        messages.success(request, "Your account has been created! You can now log in.")
        return redirect('login')  # Redirect to login after signup

    return render(request, 'signup.html')


# Chat page view
def chat(request):
    return render(request, 'chat.html')


# Privacy page view
def privacy(request):
    return render(request, 'privacy.html')


# Team page view
def team(request):
    return render(request, 'team.html')


# Logout view
def signout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')

# bot page view
def bot(request):
    return render(request, 'bot.html')
