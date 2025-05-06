from django.urls import path
from . import views

urlpatterns = [
    path('', views.fencing, name='fencing'),  # URL for the main fencing calculator page
]