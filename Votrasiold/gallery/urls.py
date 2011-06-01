from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    #(r'^/', include('gallery.urls')),
    #url(r'^$', 'Votrasi.views.index', name="index"),
    # url(r'^Votrasi/', include('Votrasi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    (r'^', 'gallery.views.index'),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
)