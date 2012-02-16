from django.http import HttpResponse, HttpRequest

def show_color(request):
	if "favorite_color" in request.COOKIES:
		return HttpResponse("Your favorite color is %s" % request.COOKIES["favorite_color"])
	else:
		return HttpResponse("You don't have a favorite color.")



def set_color(request):
	if "favorite_color" in request.GET:

		#Create an HttpResponse object....
		response = HttpResponse("Your favorite color is now %s") % request.GET(["favorite_color"])

		#....and set a cookie on the response
		response.set_cookie("favorite_color", request.GET["favorite_color"])

		return response

	else:
		return HttpResponse("You didn't gibe a favorite color.")


def test1(request):
	request.session.set_test_cookie()
	return HttpResponse("Cookie set")

def test2(request):
	request.session.delete_test_cookie()
	boolean = request.session.test_cookie_worked()

	return HttpResponse(str(boolean))