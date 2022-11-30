from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('Contact/', CommunicationListAPIView.as_view()),
    path('Contact/create', CategoryProblemCreateAPIView.as_view()),
]