from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from itertools import chain

from gameshop.main.forms import CreateGameForm, CreatePeripheryForm
from gameshop.main.models import Game, Periphery


class IndexView(views.TemplateView):
    template_name = 'main/index.html'


class DashboardView(views.ListView):
    model = Game
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = list(chain(Game.objects.all(), Periphery.objects.all()))
        return context


class GameCreateView(views.CreateView):
    template_name = 'main/create_game.html'
    form_class = CreateGameForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PeripheryCreateView(views.CreateView):
    template_name = 'main/create_periphery.html'
    form_class = CreatePeripheryForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
