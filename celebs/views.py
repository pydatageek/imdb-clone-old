from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from movies import models as movie_models
from . import models, forms

celeb_model = models.Celebrity
pagination = 10


class CelebrityIndexView(ListView):
    """
        the queryset line decreased sql queries from 175 to 7
    """
    queryset = celeb_model.objects.prefetch_related('movies_as_cast', 'movies_as_director', 'movies_as_writer', 'comments')
    template_name = 'celebs/index.html'
    context_object_name = 'celebs'
    paginate_by = pagination


class CelebrityDetail(SuccessMessageMixin, DetailView, CreateView):
    queryset = celeb_model.objects.prefetch_related('movies_as_cast', 'movies_as_director', 'movies_as_writer', 'comments')
    form_class = forms.CommentForm
    template_name = 'celebs/celeb-detail.html'
    success_message = 'your comment has been succesfully sent!'

    def get_context_data(self, **kwargs):
        context = super(CelebrityDetail, self).get_context_data(**kwargs)
        context['comment_form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse('celebs:celeb_detail', kwargs={'pk':self.object.celeb.pk, 'slug':self.object.celeb.slug})
