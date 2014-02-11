from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('recap/index.html', context_dict, context)