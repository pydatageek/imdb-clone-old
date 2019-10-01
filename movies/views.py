from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from reviews import models as review_models
from . import models, forms
 

movie_model = models.Movie
genre_model = models.Genre
pagination = 5


class MovieListMixin(ListView):
    queryset = movie_model.objects.prefetch_related(
        'writers', 'casts', 'directors', 'genres', 'imdbmovierating', 'comments')
    template_name = 'movies/index.html' 
    paginate_by = pagination


class IndexView(MovieListMixin):
    ordering = ('-release_year', 'title')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Latest movies'
        context['title_suffix'] = 'by release date'
        return context


class TopMovieList(MovieListMixin):
    ordering = ('-imdbmovierating__rating','title')

    def get_context_data(self, **kwargs):
        context = super(TopMovieList, self).get_context_data(**kwargs)
        context['title'] = 'Top movies'
        context['title_suffix'] = 'on IMDB'
        return context


class MovieDetail(SuccessMessageMixin, DetailView, CreateView):
    queryset = movie_model.objects.prefetch_related(
        'writers', 'moviecast__cast', 'directors', 'genres', 'imdbmovierating', 'comments__user')    
    form_class = forms.CommentForm
    template_name = 'movies/movie-detail.html'
    success_message = 'your comment has been sent succesfully!'

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['comment_form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse('movies:movie_detail', kwargs={'pk':self.object.movie.pk, 'slug':self.object.movie.slug})


class GenreIndexView(ListView):
    template_name = 'movies/index-genre.html'
    queryset = genre_model.objects.prefetch_related('movies')


class GenreMovieList(MovieListMixin):   
    def get_queryset(self):
        return movie_model.objects.filter(
            genres__slug__icontains=self.kwargs['slug']).order_by('-release_year', 'title').prefetch_related(
            'writers', 'casts', 'directors', 'genres', 'imdbmovierating', 'comments')

    def get_context_data(self, **kwargs):
        context = super(GenreMovieList, self).get_context_data(**kwargs)
        genre = str(self.kwargs['slug']).title()
        context['title'] = f'Latest {genre} movies'
        context['title_suffix'] = 'by release date'
        return context
