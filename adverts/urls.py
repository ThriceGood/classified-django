from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^list_adverts/(?P<cat_id>\d+)/$', 'adverts.views.list_adverts', name='list'),
    url(r'^create_advert/$', 'adverts.views.create_advert', name='create'),
    url(r'^edit_advert/(?P<advert_id>\d+)/$', 'adverts.views.edit_advert', name='edit'),
    url(r'^delete_advert/(?P<advert_id>\d+)/$', 'adverts.views.delete_advert', name='delete'),
    url(r'^display_advert/(?P<advert_id>\d+)/$', 'adverts.views.display_advert', name='display'),
    url(r'^user_adverts/(?P<user_id>\d+)/$', 'adverts.views.view_user_adverts', name='user_adverts'),
    url(r'^search/(?P<query>\d+)/$', 'adverts.views.search', name='search'),
    url(r'^save_comment/$', 'adverts.views.save_comment', name='save_comment'),
)

handler404 = 'classified.views.error404'