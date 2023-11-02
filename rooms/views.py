from .models import *
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
import re

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
    def get(self, request):