import re

from django.db import models
from django.db.models import Q
from django.urls import reverse

from celebs import models as celeb_models


class Genre(models.Model):
    date_added = models.DateTimeField('Added Date', auto_now_add=True)
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=55, unique=True)
    content = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Movie(models.Model):
    date_added = models.DateTimeField('Added Date', auto_now_add=True)

    title = models.CharField(max_length=75)
    release_year = models.CharField(max_length=4)
    slug = models.SlugField(max_length=85)

    genres = models.ManyToManyField(Genre, related_name='movies')

    duration = models.SmallIntegerField(blank=True, null=True, default=0, help_text='in minutes')
    content = models.TextField(blank=True, null=True)

    trailer = models.URLField(blank=True, null=True, default='', help_text='trailer url (for now, ONLY youtube videos)')

    casts = models.ManyToManyField(to=celeb_models.Celebrity, through='MovieCast')
    writers = models.ManyToManyField(to=celeb_models.Celebrity, related_name='writers', 
                    limit_choices_to=Q(duties__name__icontains='Writer'))
    directors = models.ManyToManyField(celeb_models.Celebrity, related_name='directors', 
                    limit_choices_to=Q(duties__name__icontains='Director'))

    source_content = models.URLField(blank=True, null=True, default='')
    source_image = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        unique_together = ('title', 'release_year')

    @property
    def summary_long(self):
        sentences = re.split("[.!?]+", str(self.content))
        sentences = '. '.join(sentences[0:2])
        return f'{sentences}.'

    @property
    def summary_long_remainder(self):
        sentences = re.split("[.!?]+", str(self.content))
        return f'{sentences[2]}.'        

    @property
    def summary_short(self):
        sentences = re.split("[.!?]+", str(self.content))
        return f'{sentences[0]}.'

    @property
    def youtube_video(self):
        """ gets youtube video specific code"""
        if str(self.trailer).find('watch?v=') > 0:
            video_url = str(self.trailer).split('watch?v=')
            return video_url[1]
        return 'video does not exist'

    # def get_absolute_url(self):
    #     return reverse('movies.views.moviedetail', args=[str(self.pk), self.slug])

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                    related_name='moviecast')
    cast = models.ForeignKey(celeb_models.Celebrity, on_delete=models.CASCADE, 
                    related_name='moviecast', limit_choices_to=Q(duties__name__icontains='Cast'))
    name = models.CharField(max_length=75, verbose_name='name in movie')

    def __str__(self):
        return self.cast.full_name
