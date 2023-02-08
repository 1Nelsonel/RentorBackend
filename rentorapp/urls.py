from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    
    path('landlords/', views.getLandLords, name='landlords'),
    path('landlord/<str:pk>/', views.getLandLord, name='landlord'),

    path('locations/', views.getLocations, name='locations'),
    path('location/<str:pk>/', views.getLocation, name='location'),

    path('property-categories/', views.getProperyCategories, name='property-categories'),
    path('property-category/<str:pk>/', views.getPropertyCategory, name='property-category'),

    path('properties/', views.getProperies, name='properties'),
    path('property/<str:pk>/', views.getProperty, name='property'),

]