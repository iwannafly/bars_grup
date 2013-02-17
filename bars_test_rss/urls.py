# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rss_reader import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # главная страница
    url(r'^$', views.main),
    # страницы c полной информацией -  в качестве poll_id будет автогенеренный
    # местным ORM id записи в БД
    url(r'^fullInfo/(?P<poll_id>\d+)/', views.showFullInfo),
    # админка
    url(r'^admin/', include(admin.site.urls)),
)
