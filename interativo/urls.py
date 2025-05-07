from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('quiz/', views.quiz, name='quiz'),
    path('galeria/', views.galeria, name='galeria'),
    path('cartinha/', views.cartinha, name='cartinha'),
]
