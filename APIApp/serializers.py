from rest_framework import serializers
from DataSource.models import VRUser,VRModel
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class VRModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= VRModel
        #fields=('name','description')
        fields = '__all__'