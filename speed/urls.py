#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import current_datetime,hours_ahead

urlpatterns = [
    # Examples:
    # url(r'^$', 'speed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'blog.views.index'),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead)
]
