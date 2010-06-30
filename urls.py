from django.conf.urls.defaults import *
import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# comment added by Tower to test the git push

urlpatterns = patterns('',
    # Example:
    # (r'^biggerscreen/', include('biggerscreen.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    #authentication
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout, {'next_page':'/plugins'}),

    # Enable the touchscreen core
    (r'^/*', include('core.urls')),

    # Enable muddle
    (r'^/*', include('muddle.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}),
)


if "screens.trac_feeds" in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'trac_feeds/', include("screens.trac_feeds.urls")),
    )

if "screens.twitter_feeds" in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'twitter_feeds/', include("screens.twitter_feeds.urls")),
    )

if "screens.rt_feeds" in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'rt_feeds/', include("screens.rt_feeds.urls")),
    )

if "screens.ftp_usersmap" in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'ftp_usersmap/', include("screens.ftp_usersmap.urls")),
    )

