from django.views.generic import ListView

from celebs import models as celeb_models
from movies import models as movie_models


class IndexView(ListView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['celebs'] = celeb_models.Celebrity.objects.prefetch_related(
            'moviecast__movie', 'directors', 'writers', 'comments'
        )[:3]
        return context

    def get_queryset(self):
        return movie_models.Movie.objects.prefetch_related(
            'writers', 'casts', 'moviecast__cast', 'directors', 'genres', 'imdbmovierating', 'comments').order_by(
            '-release_year', 'title')[:3]
