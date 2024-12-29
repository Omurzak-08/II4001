from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'post_likes', PostLikeViewSet,  basename='post_likes'),
router.register(r'comments_like', CommentLikeViewSet,  basename='comments_like'),
router.register(r'saves', SaveViewSet,  basename='saves'),
router.register(r'story', StoryViewSet,  basename='story'),
router.register(r'saves_item', SaveItemViewSet,  basename='saves_item'),

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('', PostListApiView.as_view(), name='post_list' ),
    path('post/<int:pk>/', PostDetailApiView.as_view(), name='post_detail' ),
    path('post/<int:pk>/', PostEDITApiView.as_view(), name='post_edit' ),
    path('user_profiles/', UserProfileListApiView.as_view(), name='user_profiles_list'),
    path('user_profiles/<int:pk>/', UserProfileDetailApiView.as_view(), name='user_profiles_detail'),
    path('comments/', CommentListApiView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentDetailApiView.as_view(), name='comment_detail'),
    path('follow/', FollowListApiView.as_view(), name='follow_list'),
    path('follow/<int:pk>/', FollowDetailApiView.as_view(), name='follow_detail'),
]