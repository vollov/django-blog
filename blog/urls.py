from django.conf.urls import url

from blog import views

urlpatterns = [
    #url(r'^$', views.teams, name='teams'),
    #url(r'^enroll/$', views.post_enroll, name='post_enroll'),
    url(r'^api/(?P<blog_slug>[^/]+)$', views.blog_detail_api, name='blog_detail_api'),
    url(r'^(?P<blog_slug>[^/]+)$', views.blog_detail, name='blog_detail'),
]
