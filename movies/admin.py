from django.contrib import admin

from reviews import models as review_models
from . import models, forms


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    

class MovieIbdbRatingInline(admin.TabularInline):
    model = review_models.ImdbMovieRating

    extra = 0
    max_num = 1
    min_num = 1


class MovieCastInline(admin.TabularInline):
    model = models.MovieCast


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    form = forms.MovieForm
    inlines = [MovieIbdbRatingInline, MovieCastInline,]
    
    prepopulated_fields = { 'slug': ('title', 'year') }
