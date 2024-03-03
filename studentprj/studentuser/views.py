from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse




def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account successfully created for {username}! Login in Now')
                return redirect('/login/')
    else:
          form = UserRegisterForm()

    return render(request,'studentuser/register.html',{'form':form})

@login_required
def profile(request):
        return render(request, 'studentuser/profile.html')

@login_required
def custom_logout(request):
    logout(request)
    return render(request,'studentuser/logout.html')


def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Acount Updated Successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'studentuser/profile_update.html', context)


