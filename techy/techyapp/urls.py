# urls.py
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('solutions/', views.solutions, name='solutions'),
    path('clients/', views.clients, name='clients'),
    path('partners/', views.partners, name='partners'),
    path('gallery/', views.gallery, name='gallery'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]