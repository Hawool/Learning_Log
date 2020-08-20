"""Defines patterns URL for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Output all topics
    path('topics/', views.topics, name='topics'),
    # Page with detailed information of the topic
    path('topics/<topic_id>/', views.topic, name='topic')
]
