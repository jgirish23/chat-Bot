from rest_framework import serializers
from . models import Chats

class ChatsSerializer(serializers.Serializer):
    class Meta:
        model = Chats
        fields=["Username","Text","Text_order","Check"]
