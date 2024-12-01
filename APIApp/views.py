from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,VRModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from DataSource.models import VRModel
 
User = get_user_model()
 
# Create your views here.

class getUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#class getUserVRData(generics.ListAPIView):


# Create your views here.
@api_view(['GET'])
def getVRModelData(request):
    app = VRModel.objects.all()
    serializer = VRModelSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postVRModelData(request):
    serializer = VRModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)




    


