"""Defines patterns URL for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Output all topics
    path('topics/', views.topics, name='topics'),
]
