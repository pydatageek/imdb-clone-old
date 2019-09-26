from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from movies import models as movie_models
from . import models


class CelebrityIndexView(ListView):
    model = models.Celebrity
    template_name = 'celebs/index.html'
    context_object_name = 'celebs'


class CelebrityDetail(DetailView):
    model = models.Celebrity
    template_name = 'celebs/celeb-detail.html'
    context_object_name = 'celeb'

    def get_context_data(self, **kwargs):
        # TODO
        # print also star's screen name on that movie
        context = super(CelebrityDetail, self).get_context_data(**kwargs)
        context['movies'] = movie_models.Movie.objects.filter(moviecast__cast=self.kwargs['pk'])
        return context
