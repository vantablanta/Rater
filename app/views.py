from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from api.models import Profile, Post
from .forms import RegisterForm
import requests

# Create your views here.
def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')
    context = {'page': page}
    return render(request, 'app/auth.html', context )

def register_user(request):
    form = RegisterForm()
    page = 'register'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            photo = '/static/default.png'
            bio = ""
            
    context = {'page': page, 'form': form}
    return render(request, 'app/auth.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    url = 'http://127.0.0.1:8000/api/post-list/'
    response = requests.get(url)
    posts = response.json()
    context = {'posts':posts}
    return render(request, 'app/index.html', context)

def profile(request):
   user  = request.user
   profile = Profile.objects.get(user=user)

   context = {
    'profile' : profile
   }

   return render(request, 'app/profile.html', context)