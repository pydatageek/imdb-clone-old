from django.db.models import Q
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from movies import models as movie_models
from . import models, forms


class CelebrityIndexView(ListView):
    model = models.Celebrity
    template_name = 'celebs/index.html'
    context_object_name = 'celebs'


class CelebrityDetail(DetailView, CreateView):
    model = models.Celebrity
    form_class = forms.CommentForm
    template_name = 'celebs/celeb-detail.html'
    context_object_name = 'celeb'

    def get_context_data(self, **kwargs):
        # TODO
        # print also star's screen name on that movie
        context = super(CelebrityDetail, self).get_context_data(**kwargs)
        context['movies_as_cast'] = movie_models.Movie.objects.filter(moviecast__cast=self.kwargs['pk'])
        context['movies_as_director'] = movie_models.Movie.objects.filter(directors=self.kwargs['pk'])
        context['movies_as_writer'] = movie_models.Movie.objects.filter(writers=self.kwargs['pk'])
        context['comment_form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse('celebs:celeb_detail', kwargs={'pk':self.object.celeb.pk, 'slug':self.object.celeb.slug})
