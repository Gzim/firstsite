from django.conf.urls.defaults import *


urlpatterns = patterns('',
	(r'^pic/$', 'firstsite.testapp.show_image.my_image'),
	(r'^csv/$', 'firstsite.testapp.return_csv.unruly_passengers_csv'),
	(r'^pdf/$', 'firstsite.testapp.return_pdf.hello_pdf'),
	(r'^pdf/adv/$', 'firstsite.testapp.return_pdf.hello_pdf_advanced'),
	(r'^set/cookie/$', 'firstsite.testapp.cookie_test.set_color'),
	(r'^get/cookie/$', 'firstsite.testapp.cookie_test.show_color'),
	(r'^t1/$', 'firstsite.testapp.cookie_test.test1'),
	(r'^t2/$', 'firstsite.testapp.cookie_test.test2'),
)