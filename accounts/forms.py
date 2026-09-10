from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Електронна пошта'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'avatar',
            'bio',
            'birth_date',
        )
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }