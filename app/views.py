from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.urls import resolve

import logging
logger = logging.getLogger(__name__)

def home(request):

    # Translators: This message appears on the home page only
    context = {
        'page_title': _('Home'),
        
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