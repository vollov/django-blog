from django.shortcuts import render
from blog.models import Blog
from blog.rest import BlogSerializer
#@login_required

def blog_detail(request, blog_slug):
    """show blog content as markdown - HTTP GET /blog/@blog_id
    """
    
    context = {'page_title':'blog_detail',}
#     captain = Player.objects.get(user_profile__user__id=user_id)
#     context = {'page_title':'player profile', 
#                    'captain': captain,
#                    'user_profile': captain.user_profile}
    
    return render(request, 'blog.html', context)

#################################################
# restful API
#################################################
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET',])
def blog_detail_api(request, blog_slug):
    """
    return blog detail as json data
    """
    blog = Blog.objects.get(slug=blog_slug)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

