from django.contrib.auth.forms import UserCreationForm
from django import forms

from . import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if models.User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('That email has been used before by some one else!')
    #     return self.cleaned_data

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username', 'email', 'password1', 'password2')
