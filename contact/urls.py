from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^us/$', 'firstsite.contact.views.contact_us'),
	(r'^thanks/$', 'firstsite.contact.views.contact_thanks'),
)