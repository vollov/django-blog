"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from blog.views import BlogViewSet, TagViewSet
from rest_framework import routers

api_query_blogs_by_tag = TagViewSet.as_view({'get': 'query'})
api_list_blogs = BlogViewSet.as_view({'get': 'list'})
api_blog_detail = BlogViewSet.as_view({'get': 'detail'})

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^api/v1.0/blogs/', api_list_blogs, name='api_list_blogs'),
    url(r'^api/v1.0/tag/(?P<tag_slug>[^/]+)$', api_query_blogs_by_tag, name = 'api_query_blogs_by_tag'),
    url(r'^api/v1.0/blog/(?P<blog_slug>[^/]+)$', api_blog_detail, name = 'api_blog_detail'),
    
    # base page
#     url(r'^privacy/', views.privacy, name='privacy'),
#     url(r'^terms/', views.terms, name='terms'),
#    url(r'^api/v1.0/blogs', include('blog.apis')),
    url(r'^$', views.home, name='home'),
    
    # modules urls
#     url(r'^blog/', include('blog.urls')),
#     url(r'^captcha/', include('captcha.urls')),
    
    #     url(r'^profile/', views.profile, name='profile'),
#     url(r'^rules/', views.rules, name='rules'),
#     url(r'^contacts/', views.contacts, name='contacts'),
#     
#     url(r'^team/', include('team.urls')),
#     url(r'^game/', include('game.urls')),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

# settings for development environment DEBUG
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
# if settings.DEBUG:
#     urlpatterns += [
#         url((r'^media/(?P<path>.*)','django.views.static', {'document_root': settings.MEDIA_ROOT}),'serve')
#     ]
    