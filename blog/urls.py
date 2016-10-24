from django.conf.urls import url

from team import views

urlpatterns = [
    #url(r'^$', views.teams, name='teams'),
    #url(r'^enroll/$', views.post_enroll, name='post_enroll'),
    url(r'^(?P<blog_id>[^/]+)$', views.blog_markdown, name='blog_markdown'),
    
]
