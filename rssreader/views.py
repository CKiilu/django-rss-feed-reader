from django.shortcuts import render

from .models import SourceUrl

from django.http import HttpResponse

import feedparser

# Create your views here.
def index(request):
	feeds = SourceUrl.objects.all()
	for objects in feeds:
		objects.url = feedparser.parse(objects.url + ".rss")
	context = {
		"feeds": feeds,

	}
	return render(request, "index.html", context)