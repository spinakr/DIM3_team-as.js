from django.conf.urls import patterns, include,  url
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
        url(r'(?P<project_name_url>[\w+-]*)$', views.project, name='project'),

        )