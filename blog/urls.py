from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]

#views.home utilizes the function with the httpresponse defined in views as the home page
# blog-home is name as such, since different sub apps could have different names making reverse lookup hard

#class based views look templates with certain naming conventions - <app>/<model>_<viewtype> (blog/post_list.html)
#pk defines primary key (id), variable to show which post is being viewed, int tells django to expect int, grabs the value from the url
#post_form is the template name for the create/update view
#must provide primary key for the update, django will handle rest, along with same template (post_form), including holding the data
