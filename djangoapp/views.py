from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag
# Create your views here. 

def homepage(request):
    featured_posts = Post.objects.filter(is_featured=True)
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'djangoapp/home.html', {
        'featured_posts': featured_posts,
        'posts': posts,
        'categories': categories,
        'tags': tags
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'djangoapp/post_detail.html', {'post': post})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    return render(request, 'djangoapp/category_detail.html', {'category': category, 'posts': posts})

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'djangoapp/tag_detail.html', {'tag': tag, 'posts': posts})
