from django.urls import path
from . import views
from .views import fencing_calculator

urlpatterns = [
    path('', views.fencing, name='fencing'),  # URL for the main fencing calculator page
    path('', fencing_calculator, name='fencing_calculator'),  # URL for the calculator form
]