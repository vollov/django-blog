from django.shortcuts import render
from blog.models import Blog, Tag, BlogTag
from blog.rest import BlogSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from blog.serializers import BlogSerializer, TagSerializer, BlogTagSerializer

def blog_detail(request, blog_slug):
    """show blog content as markdown - HTTP GET /blog/@blog_id
    """
    
    context = {'page_title':'blog_detail',}
#     captain = Player.objects.get(user_profile__user__id=user_id)
#     context = {'page_title':'player profile', 
#                    'captain': captain,
#                    'user_profile': captain.user_profile}
    
    return render(request, 'blog.html', context)

class BlogViewSet(viewsets.ViewSet):

    def list(self, request, format=None):
        queryset = Blog.objects.all().order_by('-views')
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

class TagViewSet(viewsets.ViewSet):
    
    def query(self, request, tag_slug, format=None):
        blogs = BlogTag.objects.get(tag__slug=tag_slug)
        serializer = BlogTagSerializer(blogs, many=True)
        return Response(serializer.data)
    
    
    