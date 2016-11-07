from blog.models import Tag, Blog, BlogTag
from rest_framework import serializers

class TagSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')
        
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=False, many=True)
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'published', 'body', 'tags', 'slug', 'author')

class BlogTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogTag
        fields = ('id', 'tag', 'blog')