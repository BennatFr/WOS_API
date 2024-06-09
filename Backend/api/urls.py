from django.urls import path
from .views import *

urlpatterns = [
    path('', APIDetailsView.as_view(), name='api_details'),
]