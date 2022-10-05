from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import PostListSerializer, PostSerializer
import json
from .models import Post, HashTag
from user.models import User
from django.db.models import Q


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
            post_obj = Post.objects.get(
                id=post_id, user_id=data["user_id"], is_active=True
            )

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
        post_obj.is_active = not post_obj.is_active
        post_obj.save()

        return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class DetailPostView(APIView):
    def get(self, request, post_id):
        """
        게시글 상세 보기 api.
        """
        post_obj = Post.objects.get(id=post_id)
        post_obj.view_count = post_obj.view_count + 1
        post_obj.save()
        serializer = PostSerializer(post_obj)

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class LikeCountPostView(APIView):
    def get(self, request, post_id):
        """
        좋아요 추가 삭제 api.
        """
        user_id = User.objects.get(email=request.user).id
        result = Post.objects.filter(id=post_id, like_count__in=[user_id])
        post_obj = Post.objects.get(id=post_id)

        print("result는 ", result)

        if result:
            """
            좋아요를 이미 눌렀으면 좋아요 취소
            """
            post_obj.like_count.remove(user_id)
        else:
            """
            좋아요 생성
            """
            post_obj.like_count.add(user_id)

        post_obj.save()

        return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class PostListView(APIView):
    def get(self, request):
        """
        게시글 목록 api.
        """
        query_set = Post.objects.all()
        serializers = PostListSerializer(query_set, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class PostSearchOrderView(APIView):
    def get(self, request):
        """
        게시글 정렬, 검색 api.
        """

        orderby = request.GET.get("orderby", None)
        search = request.GET.get("search", None)
        hashtag = request.GET.get("hashtag", None)

        query_set = Post.objects.all()

        if orderby is None:
            query_set = query_set.order_by("-created_at")

        else:
            query_set = query_set.order_by(orderby)

        if search is not None:
            search = search.replace('"', "")
            query_set = query_set.filter(
                Q(title__contains=search) | Q(content__contains=search)
            )

        if hashtag is not None:
            hashtag = hashtag.replace('"', "")
            try:
                tag_id = HashTag.objects.get(name=hashtag).id
                query_set = query_set.filter(hashtags__in=[tag_id])
            except HashTag.DoesNotExist:
                return Response(
                    {"message": "No Data"}, status=status.HTTP_201_CREATED
                )

        serializers = PostListSerializer(query_set, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)
