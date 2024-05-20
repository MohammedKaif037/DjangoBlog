from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField  # Assuming you are using CKEditor for rich text editing


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Subheading(models.Model):
    post = models.ForeignKey(Post, related_name='subheadings', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class CodeBlock(models.Model):
    post = models.ForeignKey(Post, related_name='code_blocks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    code = models.TextField()

    def __str__(self):
        return self.title if self.title else f"Code Block {self.id}"
