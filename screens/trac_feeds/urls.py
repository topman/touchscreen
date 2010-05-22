from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('screens.trac_feeds.views',
    # Example:
    # (r'^biggerscreen/', include('biggerscreen.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^get_feeds/', "get_feeds", name="trac_get_feeds"),
    
)

