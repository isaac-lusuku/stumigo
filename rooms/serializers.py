
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        time_asked = serializers.ReadOnlyField()
        fields = "__all__"
        

class SolutionSerializer(ModelSerializer):
    class Meta:
        model = Solution
        answered_at = serializers.ReadOnlyField()
        fields = "__all__"
        extra_kwargs = {"up_vote":{"write_only":True}, 
                        "down_vote":{"write_only":True}}
        

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        created_at = serializers.ReadOnlyField()
        fields = "__all__"
        

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        created_at = serializers.ReadOnlyField()
        fields = "__all__"