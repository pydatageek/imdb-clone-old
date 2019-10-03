from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from reviews import models as review_models
from . import models, forms
 

movie_model = models.Movie
genre_model = models.Genre
pagination = 5

# Views with BAD Query Scales
class MovieListMixin(ListView):
    queryset = movie_model.objects.prefetch_related('movie_crews', 'genres', 'comments')  #  'crews__moviecrew_set', 
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
    ordering = ('-imdb_rating','title')

    def get_context_data(self, **kwargs):
        context = super(TopMovieList, self).get_context_data(**kwargs)
        context['title'] = 'Top movies'
        context['title_suffix'] = 'on IMDB'
        return context


class MovieDetail(SuccessMessageMixin, DetailView, CreateView):
    queryset = movie_model.objects.prefetch_related(
        'writers', 'moviecast__cast', 'directors', 'genres', 'comments__user')    
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


class GenreMovieList(ListView):   
    template_name = 'movies/index.html' 
    paginate_by = pagination

    def get_queryset(self):
        return movie_model.objects.filter(
            genres__slug__icontains=self.kwargs['slug']).order_by('-release_year', 'title').prefetch_related(
            'movie_crews', 'genres', 'comments')

    def get_context_data(self, **kwargs):
        context = super(GenreMovieList, self).get_context_data(**kwargs)
        genre = str(self.kwargs['slug']).title()
        context['title'] = f'Latest {genre} movies'
        context['title_suffix'] = 'by release date'
        return context




# Views with GOOD Query Scales
# short for Good Query Scales is (GQ)
class MovieListMixin2(ListView):
    queryset = movie_model.objects.prefetch_related(
        'writers', 'casts', 'directors', 'genres', 'comments')
    template_name = 'movies/index2.html' 
    paginate_by = pagination


class IndexView2(MovieListMixin2):
    ordering = ('-release_year', 'title')

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        context['title'] = '(GQ) Latest movies'
        context['title_suffix'] = 'by release date'
        return context


class TopMovieList2(MovieListMixin2):
    ordering = ('-imdb_rating','title')

    def get_context_data(self, **kwargs):
        context = super(TopMovieList2, self).get_context_data(**kwargs)
        context['title'] = '(GQ) Top movies'
        context['title_suffix'] = 'on IMDB'
        return context


class GenreIndexView2(ListView):
    template_name = 'movies/index-genre2.html'
    queryset = genre_model.objects.prefetch_related('movies')


class GenreMovieList2(ListView):   
    template_name = 'movies/index2.html' 
    paginate_by = pagination

    def get_queryset(self):
        return movie_model.objects.filter(
            genres__slug__icontains=self.kwargs['slug']).order_by('-release_year', 'title').prefetch_related(
            'writers', 'casts', 'directors', 'genres', 'comments')

    def get_context_data(self, **kwargs):
        context = super(GenreMovieList2, self).get_context_data(**kwargs)
        genre = str(self.kwargs['slug']).title()
        context['title'] = f'(GQ) Latest {genre} movies'
        context['title_suffix'] = 'by release date'
        return context