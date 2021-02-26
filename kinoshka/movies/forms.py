from django.forms import ModelForm
from .models import Reviewe

class RevieweForm(ModelForm):
	class Meta(object):
		"""docstring for Meta"""
		model = Reviewe
		fields = ['name', 'email', 'message']
			