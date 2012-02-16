from django.http import HttpResponse

def my_image(request):
	image_data = open("C:/wamp/www/projekte/deindeal/template/images/HDP_0023.JPG", "rb").read()
	return HttpResponse(image_data, mimetype="image/jpg")


