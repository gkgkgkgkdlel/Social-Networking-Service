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


@permission_classes((AllowAny,))
class UpdatePostView(APIView):
    def put(self, request):
        """
        게시글 수정 api.
        """
        data = json.loads(request.body)
        user = User.objects.get(email=request.user)
        data["user_id"] = user.id
        post_id = data["post_id"]

        post_obj = None

        try:
            post_obj = Post.objects.get(id=post_id, user_id=data["user_id"])

        except Post.DoesNotExist:
            return Response(
                {"message": "NO ACCESS"}, status=status.HTTP_201_CREATED
            )

        if data.get("hashtags"):
            hashtags = data["hashtags"]
            hashtags = hashtags.split(",")
            tag_obj_list = []

            for hashtag in hashtags:
                tag, created = HashTag.objects.get_or_create(name=hashtag)
                tag_obj_list.append(tag)

            serializer = PostSerializer(post_obj, data=data)

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

        else:
            serializer = PostSerializer(post_obj, data=data)

            if serializer.is_valid():
                post_obj = serializer.save()

                return Response(
                    {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
                )

            else:
                print(serializer.errors)
                return Response(
                    {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
                )


@permission_classes((AllowAny,))
class DeletePostView(APIView):
    def delete(self, request, post_id):
        """
        게시글 삭제 api.
        """
        user_id = User.objects.get(email=request.user).id

        post_obj = None

        try:
            post_obj = Post.objects.get(id=post_id, user_id=user_id)

        except Post.DoesNotExist:

            return Response(
                {"message": "NO ACCESS"}, status=status.HTTP_201_CREATED
            )

        post_obj.delete()

        return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)
