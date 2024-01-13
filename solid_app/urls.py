# solid_app/urls.py
from django.urls import path
from .views import add_text_file_to_solid

urlpatterns = [
    path('add_text_file/', add_text_file_to_solid, name='add_text_file_to_solid'),
]
