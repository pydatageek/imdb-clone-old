from django.contrib import admin

from . import models, forms


@admin.register(models.Duty)
class DutyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    form = forms.CelebrityForm

    prepopulated_fields = { 'slug': ('first_name', 'last_name',)}
