# """
#     in this file i write all me  views to serve my API
# """

# from .models import *
# from django.db.models import Q
# from .serializers import *
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
# from rest_framework.views import APIView


# # this creates and returns the user 
# class UserView(APIView):
#     permission_classes = [AllowAny]

#     # creating a user
#     def post(self, request):
#         user_data = UserSerializer(data=request.data)
#         if user_data.is_valid():
#             user_data.save()
#             return Response(status.HTTP_201_CREATED)
#         else:
#             return Response(status.HTTP_406_NOT_ACCEPTABLE)
