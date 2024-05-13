from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import generic
from django.urls import reverse

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, Try again"))
            return redirect ('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect ('login')
    

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Your account has been created successfully!")
            return redirect(reverse('home'))  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

