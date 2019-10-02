from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    genres = models.ManyToManyField('movies.Genre', blank=True)

    def __str__(self):
        return self.get_full_name() or self.username


class UserMovieNote(models.Model):
    """
        Users have notes about their favorite movies.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    note = models.CharField(max_length=250, null=True, blank=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} ({self.movie.title})'
        