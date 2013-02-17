from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^rss_reader/', include('rss_reader.urls')),
    url(r'^$', include('rss_reader.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
