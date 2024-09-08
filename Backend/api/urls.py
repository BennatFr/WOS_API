from django.urls import path, include
from .views import *

urlpatterns = [
    path('', APIDetailsView.as_view(), name='api_details'),
    path('', include('Account.urls')),
]