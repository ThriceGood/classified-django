from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^adverts/', include('adverts.urls', namespace='adverts')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^$', 'classified.views.index', name='index'),
)
