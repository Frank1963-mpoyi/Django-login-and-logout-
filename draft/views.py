from django.shortcuts import render, redirect
#from django.contrib.auth.forms  import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        #email = form.cleaned_data.get('email')
        form.save()
        messages.success(request, f'Your account has been created ! You are now able to log in ')
        #messages.success(request, f'Account created for {username}!')
        form = UserRegistrationForm()
        return redirect('login')
        
    context ={'form': form}
    template_name = "draft/register.html"
    return render(request, template_name, context)


@login_required
def profile(request):
    u_form =  UserUpdateForm(request.POST, instance=request.user)
    p_form =  ProfileUpdateForm(request.POST, 
                                request.FILES, 
                                instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'Your Account has been updated ')                
        return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form =  ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    template_name = 'draft/profile.html'
    return render (request, template_name, context )
# encytype="multipart/form-data in profile.html save image in the background