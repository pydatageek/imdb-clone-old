from django.urls import path

from . import views as views

app_name = 'movies'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('top/', views.TopMovieList.as_view(), name='top_movies'),
    path('<int:pk>-<slug:slug>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('genre/', views.GenreIndexView.as_view(), name='genre_home'),
    path('genre/<slug:slug>/', views.GenreMovieList.as_view(), name='movies_by_genre'),
    
    path('2/', views.IndexView2.as_view(), name='home2'),
    path('2/top/', views.TopMovieList2.as_view(), name='top_movies2'),
    path('2/genre/', views.GenreIndexView2.as_view(), name='genre_home2'),
    path('2/genre/<slug:slug>/', views.GenreMovieList2.as_view(), name='movies_by_genre2'),
]
