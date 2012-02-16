from django.http import HttpResponse
from django.views.generic import list_detail
from django.shortcuts import render_to_response, get_object_or_404
from firstsite.books.models import *
from django.contrib.auth.decorators import login_required



def search_form(request):
	return render_to_response("search_form.html")

#needs to be login for using /books/search
@login_required
def search(request):
	errors = []
	if "q" in request.GET:
		q = request.GET["q"]
		if not q:
			errors.append("Enter a search term.")
		elif len(q) > 20:
			errors.append("Please enter at most 20 characters.")
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response("search_result.html", 
				{"books": books, "query" : q})
	return render_to_response("search_form.html", {"errors": errors})


#needs to be login for using /books/*publishername*
@login_required
def books_by_publisher(request, name):

	#Look up the publisher (and raise a 404 if it can't be found).
	publisher = get_object_or_404(Publisher, name__iexact=name)

	#Use the object_list view for the heavy lifting
	return list_detail.object_list(
		request,
		queryset = Book.objects.filter(publisher=publisher),
		template_name = 'books/books_by_publisher.html',
		#template_object_name = 'book',
		extra_context = {'publisher': publisher},
	)

def author_list_plaintext(request):
	response = list_detail.object_list(
		request,
		queryset = Author.objects.all(),
		mimetype = 'text/plain',
		template_name = 'books/author_list.txt',
	)
	response['Content-Disposition'] = 'attachment; filename=authors.txt'
	return response












