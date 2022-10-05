from rest_framework import serializers
from .models import Post, HashTag


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ["name"]


class PostSerializer(serializers.ModelSerializer):
    hashtags = HashTagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["title", "content", "hashtags", "user_id"]


class PostListSerializer(serializers.ModelSerializer):
    hashtags = HashTagSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.like_count.all().count()

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "hashtags",
            "like_count",
            "user_id",
            "created_at",
            "view_count",
        ]
