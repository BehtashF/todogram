from .forms import UserLoginForm,UserRegistrationForm,UserinfoSettingsForm,ProfileSettingsForm
from accounts.models import User, Profile
from rest_framework.authtoken.models import Token
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully' , 'success')
                return redirect('todo:create_task')
            else:
                messages.error(request, 'username or password incorrect', 'alert')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request , 'accounts/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            Token.objects.create(user=user)
            if user is not None:
                login(request, user)
            messages.success(request, 'you registered on this site and logged in successfully', 'success')
            return redirect('todo:create_task')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request , 'accounts/register.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out from your account', 'success')
    return redirect('core:index')
    

@login_required(login_url='accounts:login')
def user_settings(request):
    user = User.objects.get(email=request.user.email)
    profile = Profile.objects.get(user=request.user)

    # render form of user info settings
    if request.method == 'POST':
        userform = UserinfoSettingsForm(request.POST or None , instance=user)
        profileform = ProfileSettingsForm(request.POST or None , request.FILES or None, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('accounts:settings')
    else:
        userform = UserinfoSettingsForm(instance=request.user)
        profileform = ProfileSettingsForm(instance=profile)

    # render form of password change settings
    if request.method == 'POST':
        changepassform = PasswordChangeForm(request.user, request.POST)
        if changepassform.is_valid():
            changepassform.save()
            update_session_auth_hash(request, user)
            login(request, )
            messages.success(request, 'Your password was successfully updated!', success)
            return redirect('accounts:settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        changepassform = PasswordChangeForm(request.user)

    context = {
        'profile' : profile,
        'userform':userform,
        'profileform':profileform,
        'changepassform':changepassform,
    }
    return render(request, 'accounts/settings.html', context)


@login_required(login_url='accounts:login')
def remove_avatar(request):
    profile = Profile.objects.get(user=request.user)
    profile.avatar.delete()
    return redirect('accounts:settings')


#give user new token
def user_refresh_token(request):
    user_id = request.user.id
    instance = get_object_or_404(User, id=user_id)
    is_tokened = Token.objects.filter(user=instance).exists()
    if is_tokened == False:
        Token.objects.get_or_create(user=instance)
    else:
        Token.objects.filter(user=instance).delete()
        Token.objects.get_or_create(user=instance)
    return redirect('accounts:settings')
