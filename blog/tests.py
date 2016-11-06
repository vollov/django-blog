from django.test import TestCase

###############################################
## test blog model
###############################################

from blog.models import Blog, Tag, BlogTag

class TestBlog(TestCase):
    fixtures = ['auth.json','blog.json',]
    
    def test_load_blogs(self):
        blogs = Blog.objects.all()
        for blog in blogs:
            print '======{0}======{1}===='.format(blog.title, blog.author)
            for tag in blog.tags.all():
                print tag.name
            
###############################################
## test blog rest model
###############################################
from blog.rest import BlogSerializer

class TestBlogRest(TestCase):
    fixtures = ['auth.json','blog.json',]
    
    def test_load_blogs_rest(self):
        blog = Blog.objects.get(slug='how-build-node-js-blog')
        serializer = BlogSerializer(blog, many=False)
        print serializer.data
        