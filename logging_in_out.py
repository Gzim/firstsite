from django.contrib import auth
from django.http import HttpResponseRedirect

def login_view(request):
	username= request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/books/publishers/")
	else:
		#Show an error page
		return HttpResponseRedirect("/")


def logout_view(request):
	auth.logout(request)
	#Redirect to a success page.
	return HttpResponseRedirect("/")
