from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views, logout
from django.views import generic as views

from gameshop.accounts.forms import CreateProfileForm
from gameshop.common.view_mixins import RedirectToDashboard
from django.urls import reverse_lazy


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def user_logout_view(request):
    logout(request)
    return redirect('index')