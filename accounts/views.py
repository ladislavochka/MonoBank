from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import (
    ProfileForm,
    RegistrationForm,
    UserUpdateForm,
)
from .models import Profile


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = 'home'


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                'Реєстрація успішна!'
            )

            return redirect('profile')
    else:
        form = RegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


@login_required
def profile(request):
    profile_object, created = Profile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        'accounts/profile.html',
        {
            'profile_user': request.user,
            'profile': profile_object,
        }
    )


@login_required
def profile_edit(request):
    profile_object, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile_object
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(
                request,
                'Профіль успішно оновлено!'
            )

            return redirect('profile')
    else:
        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileForm(
            instance=profile_object
        )

    return render(
        request,
        'accounts/profile_edit.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    )