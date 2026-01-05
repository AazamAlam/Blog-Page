from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm form was inherited and a field was added
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #each form will be populated with current data
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your account has been updated')
            return redirect('profile') #key so it doesn't fall through again to a render and asks to refill form
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) #each form will be populated with current data
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

#decorator adds functionality to an existing function

'''
message.debug
message.info
message.sucess
message.warning
'''