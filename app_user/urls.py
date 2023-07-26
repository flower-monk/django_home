from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('sign-up/', views.user_sign_up, name='sign-up'),
]