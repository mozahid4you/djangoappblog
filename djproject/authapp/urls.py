from django.urls import path
from .views import UserCreationView


urlpatterns = [
    path('authapp/',UserCreationView.as_view(),name='register'),
]
