from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views, logout, login, authenticate
from django.views import generic as views

from gameshop.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from gameshop.accounts.models import Profile
from gameshop.common.view_mixins import RedirectToDashboard
from django.urls import reverse_lazy, NoReverseMatch


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/create_profile.html'
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


def user_logout_view(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/details_profile.html'


class ProfileEditView(views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'
    form_class = EditProfileForm

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self.request.user.id != kwargs['pk']:
            return redirect('dashboard')
        return response

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.id})


class ProfileDeleteView(views.UpdateView):
    model = Profile
    template_name = "accounts/delete_profile.html"
    form_class = DeleteProfileForm

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except NoReverseMatch:
            return redirect('dashboard')

    def get_success_url(self):
        return reverse_lazy('index')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.id})
