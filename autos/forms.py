from django.forms import ModelForm
from firstsite.autos.models import *

class Auto3Form(ModelForm):
	class Meta:
		model = Auto3
		exclude = ('user',)