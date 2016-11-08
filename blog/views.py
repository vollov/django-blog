from django.shortcuts import render
from blog.models import Blog, BlogTag
from rest_framework import viewsets
from rest_framework.response import Response
from blog.serializers import BlogSerializer, BlogTagSerializer

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
        queryset = Blog.objects.exclude(slug='about').filter(published=True).order_by('-views')
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def detail(self, request, blog_slug, format=None):
        # increment view each time
        blog = Blog.objects.get(slug=blog_slug)
        blog.views +=1
        blog.save()
        
        serializer = BlogSerializer(blog, many=False)
        return Response(serializer.data)
    
class TagViewSet(viewsets.ViewSet):
     
    def query(self, request, tag_slug, format=None):
        blog_tags = BlogTag.objects.filter(tag__slug=tag_slug)
        
        blogs = []
        # get the list of blogs
        for item in blog_tags:
            blogs.append(item.blog)
        
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    
    