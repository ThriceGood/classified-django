from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^auth/$', 'accounts.views.auth_view'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
    url(r'^invalid/$', 'accounts.views.invalid_login'),
    url(r'^register/$', 'accounts.views.register_user', name='register'),
    url(r'^register_success/$', 'accounts.views.register_success'),
    url(r'^view_profile/$', 'accounts.views.view_profile', name='view_profile'),
    url(r'^public_profile/(?P<user_id>\d+)/$', 'accounts.views.public_profile', name='public_profile'),
    url(r'^create_profile/$', 'accounts.views.create_profile', name='create_profile'),
    url(r'^edit_profile/$', 'accounts.views.edit_profile', name='edit_profile'),
    url(r'^send_message/$', 'accounts.views.send_message', name='send_message'),
    url(r'^inbox/$', 'accounts.views.inbox', name='inbox'),
    url(r'^outbox/$', 'accounts.views.outbox', name='outbox'),
)