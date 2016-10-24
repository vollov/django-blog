from django.test import TestCase

###############################################
## test blog
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
            
