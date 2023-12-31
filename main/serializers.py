# this is the python file containing my model serializer

from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token


class UserSerializer(ModelSerializer):
    class Mets:
        model = User
        id = serializers.ReadOnlyField()
        date_joined = serializers.ReadOnlyField()
        fields = "__all__"
        extra_kwags = {'password':{'write_only':True}}

class UserProfileSerializer(ModelSerializer):
    class Meta:
        user = UserSerializer()
        model = UserProfile
        fields = "__all__"


        


        