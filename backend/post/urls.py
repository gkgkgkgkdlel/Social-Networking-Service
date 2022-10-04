from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.CreatePostView.as_view()),
    path("update/", views.UpdatePostView.as_view()),
]
