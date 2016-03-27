from django import forms

from .models import SourceUrl

class FeedForm(forms.ModelForm):
	class Meta:
		model = SourceUrl
		fields = [
			"name",
			"url",
		]