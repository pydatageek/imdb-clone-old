from django import forms
from django.forms import ModelForm

from reviews import models as review_models
from . import models


class CelebrityForm(ModelForm):
    class Meta:
        model = models.Celebrity
        fields = '__all__'
        widgets = {
            'duties': forms.CheckboxSelectMultiple,
            'source_image': forms.Textarea,
        }

class CommentForm(ModelForm):
    class Meta:
        model = review_models.CelebComment
        fields = ('text', 'celeb', 'user')
        widgets = {
            'text': forms.Textarea,
            'celeb': forms.HiddenInput,
            'user': forms.HiddenInput,
        }
