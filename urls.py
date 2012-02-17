from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	(r'^$', 'firstsite.views.hello'),
	(r'^time/$', 'firstsite.views.current_datetime'),
	(r'^time/plus/(\d{1,2})/$', 'firstsite.views.hours_ahead'),
	(r'^hello/$', 'firstsite.views.hello'),
	(r'^contact/', include('firstsite.contact.urls')),
	(r'^books/', include('firstsite.books.urls')),
	(r'^test/', include('firstsite.testapp.urls')),
	(r'^autos/', include('firstsite.autos.urls')),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True,}),
	

)

#Generic Views
urlpatterns += patterns('',
	(r'^about/$', direct_to_template, {'template': 'about.html'}),
	(r'^about/(\w+)/$', 'firstsite.views.about_pages'),
)


#loggin in and out on page
urlpatterns += patterns('',
	(r'^login/$', 'django.contrib.auth.views.login', {'extra_context': {'next': '/'}}),
	(r'^logout/$', 'django.contrib.auth.views.logout', {'extra_context': {'next_page': '/login'}}),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

#register on the website
urlpatterns += patterns('',
	(r'^register/', 'firstsite.register.register'),
)

#Admin Backend
urlpatterns += patterns('',
	(r'^admin/', include(admin.site.urls)),
)

