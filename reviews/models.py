from django.conf import settings
from django.db import models

from movies import models as movie_models
from celebs import models as celeb_models


class Comment(models.Model):
    date_added = models.DateTimeField('Added Date', auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        text = str(self.text)
        return f'{self.user}: {text}'


class MovieComment(Comment):
    movie = models.ForeignKey(movie_models.Movie, on_delete=models.CASCADE, related_name='comments')


class CelebComment(Comment):
    celeb = models.ForeignKey(celeb_models.Celebrity, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name = 'Celebrity Comment'
        verbose_name_plural = 'Celebrity Comments'


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
