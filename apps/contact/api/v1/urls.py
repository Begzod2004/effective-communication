from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('Contact-api-view/', ContactListAPIView.as_view()),
    path('Contact-api-view/create', ContactCreateAPIView.as_view()),
    

]