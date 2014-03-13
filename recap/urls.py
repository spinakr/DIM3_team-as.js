from django.conf.urls import patterns, include, url
from recap import views


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'register', views.register, name='register'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^about/', views.about, name='about'),
        url(r'^changecategory/', views.change_category, name='change_category'),
        url(r'^updateindexes/', views.update_indexes, name='update_indexes'),
        url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
                       (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
                       (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/'}),
                       (r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),

        url(r'(?P<project_name_url>[\w+-]*)$', views.project, name='project'),

        )
