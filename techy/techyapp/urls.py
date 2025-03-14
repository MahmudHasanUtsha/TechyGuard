# urls.py
from django.contrib import admin
from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('email_services/', views.email_services, name='email_services'),
    path('domain_hosting/', views.domain_hosting, name='domain_hosting'),
    path('website_creation/', views.website_creation, name='website_creation'),
    path('software_development/', views.software_development, name='software_development'),
    path('hardware_purchase/', views.hardware_purchase, name='hardware_purchase'),
    path('security_solutions/', views.security_solutions, name='security_solutions'),
    path('solutions/', views.solutions, name='solutions'),
    path('clients/', views.clients, name='clients'),
    path('partners/', views.partners, name='partners'),
    path('gallery/', views.gallery, name='gallery'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]