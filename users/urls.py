from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('register/', views.RegisterView.as_view(), name='users-register'),
    path('profile/', views.profile, name='users-profile'),
    path('search_items', views.search_items, name="search_items"),
    path('rice/', views.rice_category, name='rice_category'),  # Add URL for the rice category
    path('pulses/', views.pulses_category, name='pulses_category'),  # Add URL for the pulses category
    # Add more URL patterns for other categories as needed
]

# 'users.apps.UserConfig'