from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class PostListView(ListView):
    model = Post #tells which model to query
    template_name = 'blog/home.html' #instead of <app>/<model>_<viewtype> (blog/post_list.html)
    context_object_name = 'posts' #changes the name of the variable so it matches the template, default is object list
    ordering = ['-date_posted'] #- reverses ordering

#doesn't save lines, but avoid rendering functions, and sets variables only

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    #LoginRequiredMiin is a replacement of a login required decorator but for class views
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #overrides before submission, to ensure author field is not empty (integ error)
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model =Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #UserPassesTestMixin will run this function for the user
    #purpose of this code is to forbid user changing others posts
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})