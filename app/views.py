from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

import logging
logger = logging.getLogger(__name__)


from blog.models import Blog
from service import BlogService

def home(request):
    """Listing all posts by popularity"""
    
    blogs = Blog.objects.filter(published=True).order_by('views','id')
    blogService = BlogService()

    
    context = {
        'page_title': _('Home'),
        'blogs':blogService.get_blogs_for_view(blogs),
    }
    return render(request,'home.html', context)

def privacy(request):

    context = {
        'site_name': _('site_name'),
        'page_title': _('privacy_policy'),
    }
    return render(request,'privacy.html', context)

def terms(request):

    context = {
        'site_name': _('site_name'),
        'page_title': _('terms'),
    }
    return render(request,'terms.html', context)

@login_required
def profile(request, user_id):
    """
    show user profile [GET /profile/user_id]
    """
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'page_title': _('Profile'),
    }
    return render(request,'terms.html', context)



