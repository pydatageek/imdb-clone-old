from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models, forms


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    add_form = forms.UserCreationForm

    filter_horizontal = ('genres', 'groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Favorite genres', {'fields': ('genres',)}),
    )
