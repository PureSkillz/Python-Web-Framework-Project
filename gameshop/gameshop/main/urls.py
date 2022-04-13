from django.urls import path

from gameshop.main.views import IndexView, DashboardView, GameCreateView, PeripheryCreateView, GameEditView, \
    PeripheryEditView, GameDeleteView, PeripheryDeleteView, GameDetailsView, PeripheryDetailsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('game/create/', GameCreateView.as_view(), name='create game'),
    path('game/edit/<int:pk>/', GameEditView.as_view(), name='edit game'),
    path('game/delete/<int:pk>/', GameDeleteView.as_view(), name='delete game'),
    path('game/details/<int:pk>', GameDetailsView.as_view(), name='details game'),

    path('periphery/create/', PeripheryCreateView.as_view(), name='create periphery'),
    path('periphery/edit/<int:pk>/', PeripheryEditView.as_view(), name='edit periphery'),
    path('periphery/delete/<int:pk>/', PeripheryDeleteView.as_view(), name='delete periphery'),
    path('periphery/details/<int:pk>', PeripheryDetailsView.as_view(), name='details periphery'),
)