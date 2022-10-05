from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.CreatePostView.as_view()),
    path("update/", views.UpdatePostView.as_view()),
    path("delete/<int:post_id>/", views.DeletePostView.as_view()),
    path("read/detail/<int:post_id>/", views.DetailPostView.as_view()),
    path("like_count/<int:post_id>/", views.LikeCountPostView.as_view()),
]
