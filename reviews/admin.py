from django.contrib import admin

from . import models


@admin.register(models.MovieComment)
class MovieCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CelebComment)
class CelebCommentAdmin(admin.ModelAdmin):
    pass
