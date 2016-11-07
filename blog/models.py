from __future__ import unicode_literals

from django.db import models

from django.db.models import permalink
from django.contrib.auth.models import User
import uuid
from datetime import datetime 

class Tag(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'tag'
        ordering = ['-created_at']
        
    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, {'slug': self.slug })

class Blog(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True)
    published = models.BooleanField(default=False)
    
    tags = models.ManyToManyField(Tag, through='BlogTag')
    
    created_at = models.DateTimeField(default=datetime.now, db_index=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        db_table = 'blog'
        ordering = ['-views']
        
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
    
class BlogTag(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'blog_tag'
        ordering = ['-created_at']