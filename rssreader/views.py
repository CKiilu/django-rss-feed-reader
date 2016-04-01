from django.shortcuts import render, get_object_or_404, redirect

from .models import SourceUrl
from .forms import FeedForm

from django.http import HttpResponse

import feedparser

from bs4 import BeautifulSoup


# Create your views here.
def index(request):
	form = FeedForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		print (form.cleaned_data.get("name"))
		instance.save()
	feeds = SourceUrl.objects.all()
   
	for objects in feeds:
		objects.url = feedparser.parse(objects.url)
		objects.url = objects.url.entries[0].summary_detail.value
		soup = BeautifulSoup(objects.url, 'html.parser')
		objects.url = soup.prettify()
		
	context = {
		"feeds": feeds,
		"form": form,
	}
	return render(request, "index.html", context)

def details(request, id = None):
	feeds = get_object_or_404(SourceUrl, id = id)
	
	feeds.url = feedparser.parse(feeds.url)
	feeds.url = feeds.url.entries

	for objects in feeds.url:
		soup = BeautifulSoup(objects.summary, 'html.parser')
		objects.summary = soup.prettify()

	context = {
		"feeds": feeds,
	}
	return render(request, "details.html", context)
