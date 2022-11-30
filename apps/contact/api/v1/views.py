import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db.models import Q
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg import openapi
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.contact.models import Communication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.


@api_view(['GET'])
def Communication_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CommunicationSerializer(instance=Communication.objects.all(), many=True).data, status=200)
        else:
            the_Communication = get_object_or_404(Communication, pk=pk)
            return Response(data=CommunicationSerializer(instance=the_Communication).data, status=200)
    
  

class CommunicationListAPIView(ListAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class CommunicationCreateAPIView(CreateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class CommunicationUpdateAPIView(UpdateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class CommunicationDestroyAPIView(DestroyAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


@api_view(['GET'])
def CategoryProblem_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CategoryProblemSerializer(instance=CategoryProblem.objects.all(), many=True).data, status=200)
        else:
            the_CategoryProblem = get_object_or_404(CategoryProblem, pk=pk)
            return Response(data=CategoryProblemSerializer(instance=the_CategoryProblem).data, status=200)
    
  

class CategoryProblemListAPIView(ListAPIView):
    queryset = CategoryProblem.objects.all()
    serializer_class = CategoryProblemSerializer


class CategoryProblemCreateAPIView(CreateAPIView):
    queryset = CategoryProblem.objects.all()
    serializer_class = CategoryProblemSerializer


class CategoryProblemUpdateAPIView(UpdateAPIView):
    queryset = CategoryProblem.objects.all()
    serializer_class = CategoryProblemSerializer


class CategoryProblemDestroyAPIView(DestroyAPIView):
    queryset = CategoryProblem.objects.all()
    serializer_class = CategoryProblemSerializer



