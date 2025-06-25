from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomAuthenticationForm, CustomUserCreationForm, UpdateProfileForm


# Register View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('post_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('post_list')


# Profile Page View
@login_required
def profile_page_view(request):
    return render(request, 'registration/profile.html')



# Edit Profile View
@login_required
def update_profile_view(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile Updated Successfully!')
            return render(request, 'registration/update_profile.html', {'form': form, 'success': True})
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'registration/update_profile.html', {'form': form})