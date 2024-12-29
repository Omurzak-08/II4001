from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учутные данные")


    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name']


class UserProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'



class UserProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',]



class FollowListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ['follower', 'following']


class FollowDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Follow
        fields = ['follower', 'following', 'user',]



class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['user', 'image_post', 'video_post']


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLike
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentLike
        fields = ['like']


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user',]


class CommentDetailSerializer(serializers.ModelSerializer):
    comment_like = CommentLikeSerializer()

    class Meta:
        model = Comment
        fields = [ 'user', 'text', 'parent', 'comment_like','post_comment']


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['user', 'image_story', 'video_story', 'created_at']


class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        fields = ['user']


class SaveItemSerializer(serializers.ModelSerializer):
    user = SaveSerializer(read_only=True, many=True)

    class Meta:
        model = SaveItem
        fields = ['user', 'post', 'save', 'created_date']


class PostDetailSerializer(serializers.ModelSerializer):
    comment = CommentListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['user', 'image_post', 'video_post', 'description', 'post_comment', 'hashtag', 'created_at']