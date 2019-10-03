import re

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.core.validators import ValidationError

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
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True) 

    title = models.CharField(max_length=75)
    release_year = models.CharField(max_length=4)
    slug = models.SlugField(max_length=85)

    imdb_rating = models.FloatField(blank=True, null=True, verbose_name='IMDB rating')
    duration = models.SmallIntegerField(blank=True, null=True, default=0, help_text='in minutes')
    genres = models.ManyToManyField(Genre, related_name='movies')

    content = models.TextField(blank=True, null=True)

    trailer = models.URLField(blank=True, null=True, default='', 
                    help_text='trailer url (for now, ONLY youtube videos)')
    
    # one 'crews' field takes the place of three fields ('directors', 'writers', 'casts')
    # but it shows bad query performance.
    crews = models.ManyToManyField(celeb_models.Celebrity, through='MovieCrew', related_name='movies')

    directors = models.ManyToManyField(celeb_models.Celebrity, related_name='movies_as_director', 
                    limit_choices_to=Q(duties__name__icontains='Director'))    
    writers = models.ManyToManyField(to=celeb_models.Celebrity, related_name='movies_as_writer', 
                    limit_choices_to=Q(duties__name__icontains='Writer'))
    casts = models.ManyToManyField(to=celeb_models.Celebrity, through='MovieCast')

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
                    related_name='movies_as_cast', limit_choices_to={'duties__name__icontains':'Cast'})
    name = models.CharField(max_length=75, verbose_name='name in movie')

    def __str__(self):
        return self.cast.full_name



# New model MovieCrew and its manager
# the related field on Movie is crews
# it creates more queries on pages than
# other related fields (which has the same job): 
# directors, writers and casts
# WHY?
# crews vs. directors, writers, casts
class MovieCrewManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_directors(self):
        qs = self.get_queryset()
        return qs.filter(duty__name__icontains='Director').select_related('crew')

    def get_writers(self):
        qs = self.get_queryset()
        return qs.filter(duty__name__icontains='Writer').select_related('crew')

    def get_casts(self):
        qs = self.get_queryset()
        return qs.filter(duty__name__icontains='Cast').select_related('crew')


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_crews')
    duty = models.ForeignKey(celeb_models.Duty, default=1, on_delete=models.CASCADE)
    crew = models.ForeignKey(celeb_models.Celebrity, on_delete=models.CASCADE)
    role = models.CharField(max_length=75, default='', blank=True,  
                    help_text='e.g. short story, scrrenplay for writer, voice for cast')
    screen_name = models.CharField(max_length=75, default='', blank=True,
                    help_text="crew's name on movie")

    objects = MovieCrewManager()

    def clean(self, *args, **kwargs):
        if not self.duty in self.crew.duties.all():
            raise ValidationError('crew duty and selected duty should match', code='invalid')
        super(MovieCrew, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(MovieCrew, self).save(*args, **kwargs)

    def __str__(self):
        return self.crew.full_name
