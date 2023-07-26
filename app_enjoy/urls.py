from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'/accordion', views.accordion, name='accordion'),
    path('/video', views.video, name='video')
]