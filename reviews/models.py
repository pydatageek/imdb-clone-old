from django.conf import settings
from django.db import models

from movies import models as movie_models
from celebs import models as celeb_models


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)

    class Meta:
        abstract = True


class MovieComment(Comment):
    movie = models.ForeignKey(movie_models.Movie, on_delete=models.CASCADE)


class CelebComment(Comment):
    celeb = models.ForeignKey(celeb_models.Celebrity, on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.FloatField()

    class Meta:
        abstract = True


class MovieRating(Rating):
    movie = models.OneToOneField(movie_models.Movie, on_delete=models.CASCADE)

    class Meta: 
        abstract = True


class CelebRating(Rating):
    celeb = models.ForeignKey(celeb_models.Celebrity, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UserMovieRating(MovieRating):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ImdbMovieRating(MovieRating):
    pass    


class UserCelebRating(CelebRating):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
