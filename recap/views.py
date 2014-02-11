from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import os

def index(request):
    SETTINGS_DIR = os.path.dirname(__file__)
    PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
    PROJECT_PATH = os.path.abspath(PROJECT_PATH)
    TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
    print TEMPLATE_PATH
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('recap/index.html', context_dict, context)