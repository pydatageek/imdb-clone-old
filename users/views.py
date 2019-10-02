from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView,TemplateView
from django.urls import reverse_lazy

from . import forms, models


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_success_message(self, cleaned_data):
        return f'Welcome {cleaned_data["username"]}! Thank you for joining us.'


class ProfileBaseView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    pass


class ProfileView(ProfileBaseView):
    model = models.User
    form_class = forms.CustomUserChangeForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'Your profile has been updated'

    def get_object(self):
        user = self.request.user
        return models.User.objects.get(username=user.username)


class ProfileMovieView(ProfileBaseView):
    # TODO
    # It doesn't work now!
    # This is the View that should be one page!
    model = models.UserMovieNote
    template_name = 'users/user-movies.html'

    def get_object(self):
        user = self.request.user
        return models.UserMovieNote.objects.get(user=user)
