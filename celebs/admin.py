from django.contrib import admin

from . import models, forms


@admin.register(models.Duty)
class DutyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    form = forms.CelebrityForm

    list_filter = ('duties',)
    search_fields = ('first_name', 'last_name', 'duties__name')

    prepopulated_fields = { 'slug': ('first_name', 'last_name',)}
    readonly_fields = ('added_by',)


    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
        obj.save()
