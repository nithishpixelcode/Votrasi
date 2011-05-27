from django.conf.urls.defaults import patterns, include, url

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
    (r'^', include('gallery.urls')),
)
