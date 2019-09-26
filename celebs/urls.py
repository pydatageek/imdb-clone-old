from django.urls import path

from . import views

app_name = 'celebs'

urlpatterns = [
    path('', views.CelebrityIndexView.as_view(), name='home'),
    path('<int:pk>-<slug:slug>/', views.CelebrityDetail.as_view(), name='celeb_detail'),
]
