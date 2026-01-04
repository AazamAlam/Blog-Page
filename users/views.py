from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm form was inherited and a field was added
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #with user data
        if form.is_valid():
            form.save() #saves user data (with hashing and everything)
            username = form.cleaned_data.get('username') #contains the cleaned data from the form
            messages.success(request, f'Your account has been created sucessfully!') # flash message containing sucess or failure (linked with base.html)
            #return redirect('blog-home') #redirects user to homepage
            return redirect('login')
    else:
        form = UserRegisterForm() #a blank form
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

#decorator adds functionality to an existing function

'''
message.debug
message.info
message.sucess
message.warning
'''