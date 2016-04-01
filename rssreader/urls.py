from django.conf.urls import include, url

import views

urlpatterns = [
	url(r'^$', views.index, name = "home"),
	url(r'^(?P<id>\d+)/details/$', views.details, name = "details"),
]