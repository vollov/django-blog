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
from blog.serializers import BlogSerializer

class TestBlogRest(TestCase):
    fixtures = ['auth.json','blog.json',]
    
    def test_load_blogs_rest(self):
        blog = Blog.objects.get(slug='how-build-node-js-blog')
        serializer = BlogSerializer(blog, many=False)

        expected_result = u'How to build a node js blog'
        result = serializer.data['body']
        self.assertEqual(expected_result, result)
        
###############################################
## test blog rest model
###############################################

# [
#     {
#         "id": "1",
#         "title": "How to write a blog web site with django",
#         "published": true,
#         "body": "## How to write a blog web site with django",
#         "tags": [
#             {
#                 "id": "3",
#                 "name": "Angularjs",
#                 "slug": "angularjs"
#             },
#             {
#                 "id": "1",
#                 "name": "Django",
#                 "slug": "django"
#             }
#         ],
#         "slug": "how-write-blog-web-site-django",
#         "author": "dustin"
#     },
#     {
#         "id": "2",
#         "title": "How to build a node js blog",
#         "published": true,
#         "body": "How to build a node js blog",
#         "tags": [
#             {
#                 "id": "3",
#                 "name": "Angularjs",
#                 "slug": "angularjs"
#             },
#             {
#                 "id": "2",
#                 "name": "nodejs",
#                 "slug": "nodejs"
#             }
#         ],
#         "slug": "how-build-node-js-blog",
#         "author": "dustin"
#     }
# ]
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TestBlogRestAPI(APITestCase):
    
    fixtures = ['auth.json','blog.json',]

    def test_api_list_blogs(self):
        url = reverse('api_list_blogs')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        result = [ r['title'] for r in response.data ] 
        
        expected_result = [u'How to write a blog web site with django', u'How to build a node js blog']
        self.assertEqual(expected_result, result)
        
    def test_api_blog_detail(self):
        # url = '/api/v1.0/blog/how-write-blog-web-site-django'
        url = reverse('api_blog_detail', kwargs={'blog_slug': 'how-write-blog-web-site-django'})
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected_result = u'## How to write a blog web site with django'
        result = response.data['body']
        self.assertEqual(expected_result, result)
        
    def test_api_query_blogs_by_tag(self):
        url = reverse('api_query_blogs_by_tag', kwargs={'tag_slug': 'django'})
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_result = 1
        result = response.data
        print result
        self.assertEqual(expected_result, len(result))