from django import forms
from django.conf import settings

from reviews import models as review_models
from . import models 


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = '__all__'
        widgets = {
            'source_image': forms.Textarea,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = review_models.MovieComment
        fields = ('text', 'movie', 'user')
        widgets = {
            'text': forms.Textarea(attrs={'rows':5}),
            'movie': forms.HiddenInput,
            'user': forms.HiddenInput,
        }
