from django.contrib import admin

from reviews import models as review_models
from . import models, forms


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    search_fields = ('name',)


class MovieCrewInline(admin.TabularInline):
    model = models.MovieCrew
    autocomplete_fields = ('crew',)

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    form = forms.MovieForm
    inlines = [MovieCrewInline,]
    
    list_filter = ('genres',)
    list_display = ('title', 'release_year', 'imdb_rating')

    prepopulated_fields = { 'slug': ('title', 'release_year') }
    readonly_fields = ('added_by',)
    autocomplete_fields = ('genres',)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
        obj.save()
