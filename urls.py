from django.conf.urls.defaults import *
from django.contrib import admin
#from autoregister import autoregister
import os
#autoregister('gallery')
admin.autodiscover()

urlpatterns = patterns('',
        
	#url('^admin/', include(admin.site.urls)),
	(r'^admin/filebrowser/', include('filebrowser.urls')),
	(r'^admin/(.*)', admin.site.root),
	(r'^blog/', include('blog.urls')),
	url(r'^contact-form/$', 'gallery.views.contact_form', name='contact_form'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
	(r'^',include('gallery.urls')),
	url(r'^$', 'gallery.views.index', name='index'),
)
