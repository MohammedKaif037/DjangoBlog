from django.contrib import admin

# Register your models here.
from .models import Post,Tag,Category,User,Contact
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Contact)
