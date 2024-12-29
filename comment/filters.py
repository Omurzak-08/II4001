from .models import Post
from django_filters import FilterSet

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'user': ['exact'],
            'created_at': ['gt', 'lt'],
            'hashtag': ['exact']
        }