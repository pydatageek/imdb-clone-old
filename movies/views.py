from django.db.models import Count, F
from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from reviews import models as review_models
from . import models, forms
 
"""
TODO
1. limit the listed cast number to 5 in movie-list pages
2. count the number of movies by genre
 
"""

class IndexView(ListView):
    model = models.Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    ordering = ('-release_year', 'title')


class MovieDetail(DetailView, CreateView):
    model = models.Movie
    form_class = forms.CommentForm
    template_name = 'movies/movie-detail.html'
    context_object_name = 'movie'

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['comment_form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse('movies:movie_detail', kwargs={'pk':self.object.movie.pk, 'slug':self.object.movie.slug})


class GenreList(ListView):
    # TODO
    # This is for the sidebar
    # For now genres are not shown
    model = models.Genre
    template_name = 'partial-sidebar.html'
    context_object_name = 'genres'


class GenreIndexView(ListView):
    model = models.Genre
    template_name = 'movies/index-genre.html'
    context_object_name = 'genres'

    def get_context_data(self, **kwargs):
        # TODO
        # count the number of movies by genre
        context = super(GenreIndexView, self).get_context_data(**kwargs)
        context['movie_count'] = models.Genre.objects.annotate(num_movies=Count(F('movie'))).values_list('num_movies', flat=True)
        return context

class GenreMovieList(ListView):
    model = models.Movie
    template_name = 'movies/movies-by-genre.html'
    context_object_name = 'movies'
    
    # TODO
    # I don't know get_queryset and get_context_data well
    def get_queryset(self):
        return models.Movie.objects.filter(genres__slug__icontains=self.kwargs['slug']).order_by('-release_year')

    def get_context_data(self, **kwargs):
        context = super(GenreMovieList, self).get_context_data(**kwargs)
        context['genre'] = str(self.kwargs['slug']).title()
        return context


class TopMovieList(ListView):
    model = models.Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    ordering = ('-imdbmovierating__rating','title')
