from django import forms
from .models import Question


class Contactform(forms.ModelForm):

	class Meta:
	    
		model = Question
		fields =('name', 'email', 'phone', 'message',)
