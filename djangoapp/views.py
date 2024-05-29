from django.http import HttpResponse
from django.urls import reverse
from .forms import ContactForm, LoginForm, RegisterForm
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password

@login_required
def homepage(request):
    user = request.user
    username = user.username if user.is_authenticated else None
    is_authenticated = user.is_authenticated

    searched_post = False
    searchinput = ''

    if request.method == 'POST':
        searchinput = request.POST.get('searchinput')
        posts = Post.objects.filter(
            Q(title__icontains=searchinput) |
            Q(summary__icontains=searchinput) |
            Q(content__icontains=searchinput)
        )
        searched_post = True
    else:
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    featured_posts = Post.objects.filter(is_featured=True)

    return render(request, 'djangoapp/home.html', {
        'featured_posts': featured_posts,
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'searched_post': searched_post,
        'searchinput': searchinput,
        'username': username,
        'is_authenticated': is_authenticated,
    })

@csrf_exempt
def post_detail(request, pk):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'djangoapp/post_detail.html', {'post': post, 'tags': tags, 'categories': categories})

@csrf_exempt
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    return render(request, 'djangoapp/category_detail.html', {'category': category, 'posts': posts})

@csrf_exempt
def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'djangoapp/tag_detail.html', {'tag': tag, 'posts': posts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'djangoapp/contact.html', {'form': form})

def about_view(request):
    return render(request, 'djangoapp/about.html')

def save_contactdata(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = f'Thank you for contacting us, {request.POST.get("name")}'
            return redirect('home', {'message': message})
    else:
        form = ContactForm()
    return render(request, 'djangoapp/contact.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('login')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists", status=400)

        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password)
        user.save()

        return redirect('login')
    else:
        return render(request, 'djangoapp/register.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next') or request.POST.get('next') or 'home'
                return redirect(next_url)
            else:
                return render(request, 'djangoapp/login.html', {'form': form, 'error': 'Invalid credentials'})
    return render(request, 'djangoapp/login.html', {'form': form})

from .forms import PostForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save the many-to-many fields (tags)
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'djangoapp/create_post.html', {'form': form})