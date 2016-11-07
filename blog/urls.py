from django.conf.urls import url

from blog import views

urlpatterns = [
    #url(r'^enroll/$', views.post_enroll, name='post_enroll'),
    url(r'^(?P<blog_slug>[^/]+)$', views.blog_detail, name='blog_detail'),
]
