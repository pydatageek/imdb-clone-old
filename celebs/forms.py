from django import forms
from django.conf import settings

from reviews import models as review_models
from . import models


class CelebrityForm(forms.ModelForm):
    class Meta:
        model = models.Celebrity
        fields = '__all__'
        widgets = {
            'duties': forms.CheckboxSelectMultiple,
            'source_image': forms.Textarea,
        }

    # def clean_added_by(self):
    #     if not self.cleaned_data['added_by']:
    #         return settings.AUTH_USER_MODEL
    #     return self.cleaned_data['added_by']

    # def save(self, *args, **kwargs):
    #     self.added_by = self.request['user']
    #     form = super(CelebrityForm, self).save(*args, **kwargs)
    #     form.save()
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = review_models.CelebComment
        fields = ('text', 'celeb', 'user')
        widgets = {
            'text': forms.Textarea(attrs={'rows':5}),
            'celeb': forms.HiddenInput,
            'user': forms.HiddenInput,
        }
