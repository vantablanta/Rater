from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from api.models import Profile, Post, Rating
from .forms import RegisterForm
from .forms import RatingsForm, SubmitForm, UpdateProfileForm

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

            profile = Profile.objects.create(user=user)
            profile.save()

            return redirect('login') 
    context = {'page': page, 'form': form}
    return render(request, 'app/auth.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    single_post = Post.objects.last()
    posts = Post.objects.all()
    context = {'post':single_post, 'posts':posts}
    return render(request, 'app/index.html', context)

@login_required(login_url='/login')
def profile(request):
   user  = request.user
   profile = Profile.objects.get(user=user)

   context = {
    'profile' : profile
   }

   return render(request, 'app/profile.html', context)

@login_required(login_url='/login')
def add_post(request):
    form = SubmitForm()
    user = request.user
    owner = Profile.objects.get(user=user) 
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            url = form.cleaned_data['post_url']
            upload = Post(image=image, title=title, description=description, owner=owner, post_url=url)
            upload.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'app/add.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)
        )
        context = {'posts': posts}
        return render(request, 'app/search.html', context)

@login_required(login_url='/login')
def project(request, post):
    post = Post.objects.filter(title=post).first()
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    context = {
        'post': post,
        'form': form,
        'rating_status': rating_status

    }
    return render(request, 'app/project.html', context)

@login_required(login_url='/login')
def update_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = UpdateProfileForm(request.POST,request.FILES, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'app/update.html', context)