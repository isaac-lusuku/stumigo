# this is the python file containing my model serializer

from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers


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


        

from .models import *
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
import re



# function to validat the email address that was entered 
def is_valid_email(email):
    # Define a regular expression for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# this creates and returns the user 
class UserView(APIView):
    permission_classes = [AllowAny]

        