from rest_framework import serializers

from blog.models import Blog, Tag, BlogTag
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class BlogSerializer(serializers.ModelSerializer):
    #author = serializers.StringRelatedField(many=False)
    #     tracks = serializers.HyperlinkedRelatedField(
    #         many=True,
    #         read_only=True,
    #         view_name='track-detail'
    #     )
    author = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'views', 'author', 'created_at')