from django.test import TestCase

import logging
log = logging.getLogger(__name__)

###############################################
## test blog model
###############################################

from blog.models import Blog, Tag, BlogTag

class TestBlog(TestCase):
    fixtures = ['auth.json','blog.json',]
    
#     @classmethod
#     def setUpClass(cls):
#         log.debug('################################')
#         log.debug('# Test Blog data module')
#         log.debug('################################')
#     
#     @classmethod
#     def tearDownClass(cls):
#         pass
#     
#     def setUp(self):
#         print 'xxx'
        
    def test_load_blogs(self):
        blogs = Blog.objects.all()
        
        self.assertEqual(len(blogs), 2, 'there should be {0} blogs in the database'.format(len(blogs)))
        
#         for blog in blogs:
#             print '======{0}======{1}===='.format(blog.title, blog.author)
#             for tag in blog.tags.all():
#                 print tag.name
            
    def test_blog_2(self):
        print 'test blog 2\n'
        self.assertEqual(2, 2, 'incorrect default size')
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
        