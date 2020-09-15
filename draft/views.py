from django.shortcuts import render, redirect
#from django.contrib.auth.forms  import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


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
    template_name = 'draft/profile.html'
    return render (request, template_name )
