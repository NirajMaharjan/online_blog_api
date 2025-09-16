from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Post, Comment, Like

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}  # don’t return password
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value
    def create(self, validated_data):
        # hash the password before saving
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # to show user's username instead of ID
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ["user", "created_at"]
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")  # to show author's username instead of ID
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]
        
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # to show author's username instead of ID
    likes_count = serializers.SerializerMethodField()  # to show number of likes
    comments_count = serializers.SerializerMethodField()  # to show number of comments
    
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    
    
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]