from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

# Model is registered, so it can be accessed through the admin page