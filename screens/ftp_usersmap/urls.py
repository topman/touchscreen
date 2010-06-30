from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('screens.ftp_usersmap.views',
    # Example:
    # (r'^biggerscreen/', include('biggerscreen.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^get_user_info/$', "get_user_info", name="ftp_user_info"),
    
)

