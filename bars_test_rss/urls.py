from django.conf.urls import patterns, include, url
from rss_reader import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^rss_reader/', include('rss_reader.urls')),
    url(r'^$', views.main),
    url(r'^get_hostname/(?P<poll_id>\d+)/', views.showFullInfo),
    url(r'^admin/', include(admin.site.urls)),
)
