from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models, forms


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.CustomUserChangeForm
    