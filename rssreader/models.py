from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class SourceUrl(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	url = models.URLField(max_length = 200, unique = True)
	last_visited = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("rssreader:details", kwargs={"id": self.id})