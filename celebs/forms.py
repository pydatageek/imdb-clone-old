from django import forms
from django.forms import ModelForm

from . import models


class CelebrityForm(ModelForm):
    class Meta:
        model = models.Celebrity
        fields = '__all__'
        widgets = {
            'duties': forms.CheckboxSelectMultiple,
            'source_image': forms.Textarea,
        }
