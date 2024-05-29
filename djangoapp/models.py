from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField  # Assuming you are using CKEditor for rich text editing
from django.contrib.auth import get_user_model

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("tag-detail", kwargs={"pk": self.pk})
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

 
