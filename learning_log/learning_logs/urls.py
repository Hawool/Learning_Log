"""Defines patterns URL for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Output all topics
    path('topics/', views.topics, name='topics'),
    # Page with detailed information of the topic
    path('topics/<topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    # Page for edit entries
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
