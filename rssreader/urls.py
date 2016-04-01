from django.conf.urls import include, url

import views

urlpatterns = [
	url(r'^$', views.index, name = "home"),
	url(r'^create/$', views.post_create, name="create"),
	url(r'^(?P<id>\d+)/details/$', views.details, name = "details"),
	url(r'^(?P<id>\d+)/details/delete/$', views.post_delete, name="delete"),
]