from django.http import HttpResponse
from django.urls import reverse
from .forms import ContactForm, LoginForm, RegisterForm
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag, User
from django.views.decorators.csrf import csrf_exempt
# Create your views here. 
from django.db.models import Q

def homepage(request):
    searched_post = False  # Initialize with a default value
    searchinput = ''  # Initialize with a default value
    if request.method == 'POST':
        searchinput = request.POST.get('searchinput')
        posts = Post.objects.filter(
            Q(title__icontains=searchinput) |
            Q(summary__icontains=searchinput) |
            Q(content__icontains=searchinput)
        )
        searched_post=True
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
            message=f'Thank you for Contact {request.POST.get('name')}'
            return redirect('home',{'message': message})
    else:
        form = ContactForm()
    return render(request, 'djangoapp/contact.html', {'form': form})

    
def homepage(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        username = user.username  # Get the username from the user object
    else:
        username = None

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
        'username': username,  # Pass the username to the template
        'is_authenticated': request.user.is_authenticated,  # To display  login or logout on home
    })

def logout_view(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login')

from django.contrib.auth.hashers import make_password, check_password

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists", status=400)

        # Hash the password before saving
        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password)
        user.save()

        return redirect('login')
    else:
        return render(request, 'djangoapp/register.html',{'form':form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id  # Store user ID in session
                return redirect('home')
            else:
                return HttpResponse("Invalid credentials", status=401)
        except User.DoesNotExist:
            return HttpResponse("Invalid credentials", status=401)
    else:
        return render(request, 'djangoapp/login.html',{'form':form})
        

