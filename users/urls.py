from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy

from .views import UserCreateView, HomeView

app_name = 'users'

urlpatterns = [
    # TODO: wrong success (redirect?) url
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     next_page=reverse_lazy('users:home'),
                                     ), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),

    path('home/', HomeView.as_view(), name='home'),

]
