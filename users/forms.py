from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm, inlineformset_factory

from movies.models import Movie
from .models import User, UserMovie


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'genres')
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }


class UserMovieForm(ModelForm):
    genre = forms.HiddenInput()

    # def __init__(self, *args, user, **kwargs):
    #     self.user = user
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = UserMovie
        fields = ('user', 'movie', 'note', 'watched', 'watch_list')
        widgets = {
            'user': forms.HiddenInput,
            'movie': forms.HiddenInput,
            'watched': forms.CheckboxInput(),
        }

UserMovieFormSet = inlineformset_factory(Movie, UserMovie, 
        form=UserMovieForm, extra=1, can_delete=True)


class UserMovieFormWithLoop(ModelForm):
    genre = forms.HiddenInput(attrs={'disabled': True})

    class Meta:
        model = UserMovie
        fields = ('user', 'movie', 'note', 'watched', 'watch_list')
        widgets = {
            'user': forms.HiddenInput,
            'movie': forms.HiddenInput,
            'watched': forms.CheckboxInput(),
        }
