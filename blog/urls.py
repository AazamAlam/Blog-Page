from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]

#views.home utilizes the function with the httpresponse defined in views as the home page
# blog-home is name as such, since different sub apps could have different names making reverse lookup hard