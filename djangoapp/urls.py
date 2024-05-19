from djangoapp import views
from django.urls import path


urlpatterns = [
    path('home', views.homepage, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('category/<int:pk>/', views.category_detail, name='category-detail'),
    path('tag/<int:pk>/', views.tag_detail, name='tag-detail'),
]
