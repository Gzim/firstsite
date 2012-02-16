from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page
import datetime


from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from django.contrib import auth


def about_pages(request, page):
	try:
		return direct_to_template(request, template="about/%s.html" % page)
	except TemplateDoesNotExist:
		raise Http404()


@cache_page(60*15)
def hello(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	#return HttpResponse('<table>%s</table>' % '\n'.join(html))
	return HttpResponse("HELLO SALI")

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_time.html', {'current_date': now, 'user': request.user})
   

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('future_time.html', {'next_time': dt, "hour_offset": offset})
    
 