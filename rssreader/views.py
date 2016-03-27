from django.shortcuts import render

from .models import SourceUrl
from .forms import FeedForm

from django.http import HttpResponse

import feedparser

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
	context = {
		"feeds": feeds,
		"form": form,
	}
	return render(request, "index.html", context)