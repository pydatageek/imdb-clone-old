from django import forms
from django.forms import ModelForm

from . import models 


class MovieForm(ModelForm):
    class Meta:
        model = models.Movie
        fields = '__all__'
        widgets = {
            'source_image': forms.Textarea,
        }
