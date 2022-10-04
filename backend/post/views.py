from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import PostSerializer
import json
import bcrypt
import re
from .models import Post, HashTag
from user.models import User


@permission_classes((AllowAny,))
class CreatePostView(APIView):
    def post(self, request):
        """
        게시글 생성 api.
        """
        # email = request.data["email"]
        # password = request.data["password"]
        # name = request.data["name"]
        data = json.loads(request.body)
        user = User.objects.get(email=request.user)
        data["user_id"] = user.id

        hashtags = data["hashtags"]
        hashtags = hashtags.split(",")
        tag_obj_list = []

        for hashtag in hashtags:
            tag, created = HashTag.objects.get_or_create(name=hashtag)
            tag_obj_list.append(tag)

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            post_obj = serializer.save()
            for tag_obj in tag_obj_list:
                post_obj.hashtags.add(tag_obj)

            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        else:
            print(serializer.errors)
            return Response(
                {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
            )
