from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    #(r'^/', include('gallery.urls')),
    #url(r'^$', 'Votrasi.views.index', name="index"),
    # url(r'^Votrasi/', include('Votrasi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    (r'^', 'gallery.views.index'),
    
)