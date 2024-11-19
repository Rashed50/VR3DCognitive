from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
User = get_user_model()
 
# Create your views here.

class getUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class getUserVRData(generics.ListAPIView):
    ab =100


    


