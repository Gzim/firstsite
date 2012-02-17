from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^search/$', 'firstsite.autos.views.show_users_and_search'),
	(r'^result/(\w+)/$', 'firstsite.autos.views.show_offers_of_user'),
	(r'^addcar/$', 'firstsite.autos.views.add_a_car'),
	(r'^showcars/$', 'firstsite.autos.views.list_cars_for_editing'),

)