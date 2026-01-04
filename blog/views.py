from django.shortcuts import render
from .models import Post
'''
posts = [
    {
        'author': 'Corey',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
#Dummy data
'''

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#render is a shortcut that takes in the request and path as parameters
#3rd argument is context, fo passing mroe information
#view is still returning an http response (or exception)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})