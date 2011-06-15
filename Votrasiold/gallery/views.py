from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from gallery.models import *
def index(request):
    category_list   =ImageCategory.objects.all()
    context         ={'category':category_list }
    return render_to_response ('index.html', context, context_instance = RequestContext(request))
   