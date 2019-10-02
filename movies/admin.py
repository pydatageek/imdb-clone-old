from django.contrib import admin

from reviews import models as review_models
from . import models, forms


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    search_fields = ('name',)


class MovieCastInline(admin.TabularInline):
    model = models.MovieCast
    autocomplete_fields = ('cast',)


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    form = forms.MovieForm
    inlines = [MovieCastInline,]
    
    list_filter = ('genres',)
    list_display = ('title', 'release_year', 'imdb_rating')

    prepopulated_fields = { 'slug': ('title', 'release_year') }
    readonly_fields = ('added_by',)
    autocomplete_fields = ('genres',)
    filter_horizontal = ('writers', 'directors')

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
        obj.save()
