from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy

from .views import UserCreateView, AccountView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     next_page=reverse_lazy('products:product-list'),
                                     ), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),

    path('account/', AccountView.as_view(), name='account'),

]
