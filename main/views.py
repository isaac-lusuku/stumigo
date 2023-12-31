from __future__ import print_function
"""
    in this file i write all me  views to serve my API
"""

from .models import *
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
import re

"""
    THE FEATURE THAT I AM LEFT WITH IN THIS FILE
-> i have to write a program that sends the user a validatiion eamail before 
they can be fully regstered 
"""



# function to validat the email address that was entered 
def is_valid_email(email):
    # Define a regular expression for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# this creates and returns the user 
class UserView(APIView):
    permission_classes = [AllowAny]

    # creating a user
    def post(self, request):
        user_data = UserSerializer(data=request.data)

        # validating the email address entered 
        if is_valid_email(request.email):
            """
            after this point i should consider a verification email for 
            confirmation
            """
            if user_data.is_valid():
                user_data.save()
                return Response(status.HTTP_201_CREATED)
            else:
                return Response(status.HTTP_406_NOT_ACCEPTABLE)
        
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer_data = UserProfileSerializer(user, many=False).data
        return Response(serializer_data, status.HTTP_200_OK)
        

