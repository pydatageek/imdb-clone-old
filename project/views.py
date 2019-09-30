from django.views.generic import ListView

from celebs import models as celeb_models
from movies import models as movie_models


class IndexView(ListView):
    model = movie_models.Movie
    template_name = 'index.html'
    context_object_name = 'movies'
    # ordering = ('-year', 'title')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['celebs'] = celeb_models.Celebrity.objects.all()[:3]
        return context

    def get_queryset(self):
        return movie_models.Movie.objects.order_by('-release_year', 'title')[:3]
