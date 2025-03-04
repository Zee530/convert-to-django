from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('apply/', views.apply, name='apply'),
    path('program/', views.program, name='program'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.registerUser, name='registerUser')
    ]