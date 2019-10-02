from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from . import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email', 'genres')
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }
