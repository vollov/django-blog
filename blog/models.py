from __future__ import unicode_literals

from django.db import models

from django.db.models import permalink
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return self.name
    
    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, {'slug': self.slug })

class Blog(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    tag = models.ForeignKey('Tag')
    views = models.IntegerField(default=0)
    author = models.OneToOneField(User, null=True)

    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
    
