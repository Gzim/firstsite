from django.shortcuts import render_to_response
from firstsite.contact.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def contact_us(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			message = u'**************************************' + u'\n' +\
				u'Vorname:\t' + cd['firstname'] + u'\n' + \
				u'Nachname:\t' + cd['lastname'] + u'\n' + \
				u'E-Mail:\t' + cd['email'] + u'\n' +\
				u'**************************************' + \
				u'\n' + cd['message']
			send_mail(
				cd['subject'],
				message,
				cd.get('email'),
				['gzimzimberi@hotmail.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'I Love Your Site!'}
		)

	return render_to_response('contact/contact_form.html', {'form': form})


def contact_thanks(request):
	return render_to_response('contact/thanks.html')

