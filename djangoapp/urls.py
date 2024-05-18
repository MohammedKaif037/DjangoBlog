from djangoapp import views
from django.urls import path


urlpatterns = [
    path('',views.homepage),
    
]
