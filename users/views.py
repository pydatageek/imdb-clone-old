from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from . import forms


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_success_message(self, cleaned_data):
        return f'Welcome {cleaned_data["username"]}! Thank you for joining us.'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
