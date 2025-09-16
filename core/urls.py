from django.urls import path
from .views import RegisterView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("posts/", views.PostListCreateView.as_view(), name="post_list_create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:post_id>/comments/", views.CommentListCreateView.as_view(), name="comment_list_create"),
    path("posts/<int:post_id>/comments/<int:pk>/", views.CommentDetailView.as_view(), name="comment_detail"),
    path("posts/<int:post_id>/like/", views.LikeCreateView.as_view(), name="like_create"),
    path("posts/<int:post_id>/unlike/", views.LikeDeleteView.as_view(), name="like_delete"),
]