from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from itertools import chain
from random import shuffle
from django.contrib.auth import mixins as auth_mixins

from gameshop.main.forms import CreateGameForm, CreatePeripheryForm, EditGameForm, EditPeripheryForm, DeleteGameForm, \
    DeletePeripheryForm
from gameshop.main.models import Game, Periphery


class IndexView(views.TemplateView):
    template_name = 'main/index.html'


class DashboardView(views.ListView):
    model = Game
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = list(chain(Game.objects.all(), Periphery.objects.all()))
        shuffle(context['items'])
        return context


# Mixins ---------------------------------------


class CreateViewMixin(auth_mixins.LoginRequiredMixin,  views.CreateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditViewMixin(auth_mixins.LoginRequiredMixin, views.UpdateView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        item_class = self.form_class.Meta.model
        if self.request.user.id != item_class.objects.get(pk=kwargs['pk']).user_id:
            return redirect('login user')
        return response

    def get_success_url(self):
        return reverse_lazy(f'details {self.object.get_class_name().lower()}', kwargs={'pk': self.object.id})


class DetailsViewMixin(views.DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


# Game ---------------------------------------------


class GameCreateView(CreateViewMixin):
    template_name = 'main/create_game.html'
    form_class = CreateGameForm
    success_url = reverse_lazy('dashboard')


class GameEditView(EditViewMixin):
    model = Game
    template_name = "main/edit_item.html"
    form_class = EditGameForm


class GameDeleteView(EditViewMixin):
    model = Game
    template_name = "main/delete_item.html"
    form_class = DeleteGameForm


class GameDetailsView(DetailsViewMixin):
    model = Game
    template_name = "main/details_item.html"


# Periphery ---------------------------------------------


class PeripheryCreateView(CreateViewMixin):
    template_name = 'main/create_periphery.html'
    form_class = CreatePeripheryForm
    success_url = reverse_lazy('dashboard')


class PeripheryEditView(EditViewMixin):
    model = Periphery
    template_name = "main/edit_item.html"
    form_class = EditPeripheryForm


class PeripheryDeleteView(EditViewMixin):
    model = Periphery
    template_name = "main/delete_item.html"
    form_class = DeletePeripheryForm


class PeripheryDetailsView(DetailsViewMixin):
    model = Periphery
    template_name = "main/details_item.html"
