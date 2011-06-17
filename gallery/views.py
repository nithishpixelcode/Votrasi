from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from gallery.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    
    category_list   =Category.objects.all()
    context         ={'category':category_list }
    return render_to_response ('index.html', context, context_instance = RequestContext(request))
   
def gallery(request,name):
    images          =CategoryImage.objects.filter(image_category=name) 
    ic=Category.objects.get(category_name=name)
    catinfo = ic.category_description
    catname=ic.category_name
    context         ={'imageslist':images,'catinfo':catinfo,'catname':catname}
    return render_to_response ('images.html',context,context_instance=RequestContext(request))
