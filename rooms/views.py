from .models import *
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
import re
import jwt
from main.models import *

# the function that returns the authenticated user
"""
# this is the command that calls it
   -->email = auth_user(request.META.get('HTTP_AUTHORIZATION')) <--
"""
def auth_user(token):
    
        authorization_header = token
        if authorization_header and authorization_header.startswith('Bearer '):
            token = authorization_header.split(' ')[1]
            SECRET_KEY = 'django-insecure--p2@(3we42aui0o1*=4_f%(yn6zcm&@vcuc)lf_s-dvj$m2^1&'
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                return (payload.get("email"))
            except Exception as e:
                return False
        else:
            return False


class TopicView(APIView):
    permission_classes = [IsAuthenticated]

    # to get all the topics that exist
    def get(self, request):
        topics = Topic.objects.all()
        topic_serializer = TopicSerializer(topics, many=True)
        return Response(topic_serializer.data, status.HTTP_200_OK)
    
    # to add a new topic
    def post(self, request):
        topic = TopicSerializer(data=request.data)
        if topic.is_valid():
            topic.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_406_NOT_ACCEPTABLE)

 
# the room view        
class RoomView(APIView):
    permission_classes = [IsAuthenticated]

    # creatng a room
    def post(self, request):
        room  = RoomSerializer(data=request.data)
        if room.is_valid():
            room.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_406_NOT_ACCEPTABLE)
        
    # getting a room
    def get(self, request, pk):
        room = Room.objects.get(id= pk)

        # getting the roo messages
        messages = room.message_set.all().order_by("-time_created")
        message_serializer = MessageSerializer(messages, many=True)

        if room:
            room_serializer = RoomSerializer(room, many=False)
            message_room = {
                "room":room_serializer.data,
                "messages":message_serializer.data,
            }
            return Response(message_room, status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
        

# a view to deal with individual the messgaes
class MessageView(APIView):
     permission_classes = [IsAuthenticated]

    #  creating a message
     def post(self, request):
         message = MessageSerializer(data=request.data)
         if message.is_valid():
             message.save()
             return Response(status.HTTP_200_OK)
         else:
             return Response(status.HTTP_406_NOT_ACCEPTABLE)
         
    # editting a message
     def put(self, request, pk):
         pass
     
     
# a view to deal with individual the messgaes
class MessageView(APIView):
     permission_classes = [IsAuthenticated]

    #  creating a message
     def post(self, request):
         message = MessageSerializer(data=request.data)
         if message.is_valid():
             message.save()
             return Response(status.HTTP_200_OK)
         else:
             return Response(status.HTTP_406_NOT_ACCEPTABLE)
         
    # editting a message
     def put(self, request, pk):