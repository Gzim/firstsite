from django.conf.urls.defaults import *

from django.views.generic import list_detail
from firstsite.books.models import *

urlpatterns = patterns('',
	#(r'^search-form/$', search_form),
	(r'^search/$', 'firstsite.books.views.search'),
)


publisher_info = {
	'queryset': Publisher.objects.all(),
	#'template_object_name': 'publisher',
	'extra_context': {'book_list': Book.objects.all()},
}

book_info = {
	'queryset': Book.objects.order_by('-publication_date'),
}


urlpatterns += patterns('',
	(r'^publishers/$', list_detail.object_list, publisher_info),
	(r'^books/$', list_detail.object_list, book_info),
	(r'^(\w+)/$', 'firstsite.books.views.books_by_publisher'),

	(r'^downlaodauthors/$', 'firstsite.books.views.author_list_plaintext'),

)