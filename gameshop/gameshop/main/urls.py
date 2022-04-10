from django.urls import path

from gameshop.main.views import IndexView, DashboardView, GameCreateView, PeripheryCreateView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('game/create/', GameCreateView.as_view(), name='create game'),
    path('periphery/create/', PeripheryCreateView.as_view(), name='create periphery'),
)