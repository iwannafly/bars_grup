from django.conf.urls import  *
from rss_reader.views import main

urlpatterns = patterns('',
    url(r'^$', main),
)