from django.shortcuts import render, get_object_or_404, redirect

from .models import SourceUrl
from .forms import FeedForm

from django.http import HttpResponse, HttpResponseRedirect

import feedparser

from django.template import Template, Context

from bs4 import BeautifulSoup


# Create your views here.
def index(request):
	
	feeds = SourceUrl.objects.all()
   
	for objects in feeds:
		objects.url = feedparser.parse(objects.url)
		objects.url = objects.url.entries[0].summary_detail.value
		soup = BeautifulSoup(objects.url, 'html.parser')
		objects.url = soup.prettify()
		
	context = {
		"feeds": feeds,
	}
	return render(request, "index.html", context)

def details(request, id = None):
	feeds = get_object_or_404(SourceUrl, id = id)
	
	feeds.url = feedparser.parse(feeds.url)
	feeds_url = feeds.url.entries

	entries = []
	delete = "Delete Feed"
	delete_button = Template("""
			<a href="{{ instance.get_absolute_url }}delete/ " class="button">{{ delete }}</a>
			""").render(Context({"delete": delete}))

	for objects in feeds_url:
		soup = BeautifulSoup(objects.summary, 'html.parser')
		objects.summary = soup.prettify()
		objects.summary = objects.summary
		entries.append(objects.summary)

	context = {
		"feeds": feeds,
		"feeds_url": feeds_url,
		"entries": entries,
		"delete_button": delete_button,
	}
	return render(request, "details.html", context)

def post_delete(request,id=None):
	instance = get_object_or_404(SourceUrl, id=id)
	instance.delete()
	return redirect("rssreader:home")

def post_create(request):
	# if not request.user.is_authenticated():
	# 	raise Http404


	form = FeedForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		print (form.cleaned_data.get("name"))
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
	"form": form,
	}
	return render(request, "add_feed.html", context)