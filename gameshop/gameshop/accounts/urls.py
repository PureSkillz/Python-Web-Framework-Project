from django.urls import path

from gameshop.accounts.views import UserRegisterView, UserLoginView, user_logout_view, ProfileDetailsView

urlpatterns = (
    path('login/', UserLoginView.as_view(redirect_authenticated_user=True), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('logout/', user_logout_view, name='logout user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='details user'),
)