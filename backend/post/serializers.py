from rest_framework import serializers
from .models import Post, HashTag


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ["title", "content", "hashtags", "user_id"]


class PostSerializer(serializers.ModelSerializer):
    hashtags = HashTagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["title", "content", "hashtags", "user_id"]
