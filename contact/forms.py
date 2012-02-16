from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(required=True, max_length=100)
	firstname = forms.CharField(required=False, max_length=50, label="Vorname")
	lastname = forms.CharField(required=False, max_length=50, label="Nachname")
	email = forms.EmailField(required=False, label="Your E-Mail address")
	message = forms.CharField(required=True, widget=forms.Textarea)


	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message