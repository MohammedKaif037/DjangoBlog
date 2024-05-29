from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from djangoapp import views 

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('category/<int:pk>/', views.category_detail, name='category-detail'),
    path('tag/<int:pk>/', views.tag_detail, name='tag-detail'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this line
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('contact/savecontactdata', views.save_contactdata, name='save_contactdata'),
    path('register/register', views.register_view, name='register_register'),
    path('create-post/', views.create_post, name='create-post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)