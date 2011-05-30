from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from autoregister import autoregister
autoregister('gallery')
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    #(r'^/', include('gallery.urls')),
    #url(r'^$', 'Votrasi.views.index', name="index"),
    # url(r'^Votrasi/', include('Votrasi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
 
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^$', include('gallery.urls')),
)
