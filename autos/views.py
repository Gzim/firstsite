from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist




def show_users_and_search(request):
	all_users = User.objects.all()

	errors = []
	if "q" in request.GET:
		q = request.GET["q"]
		if not q:
			errors.append("Enter a search term.")
		else:
			autos = User.objects.filter(username__icontains=q)
			return HttpResponseRedirect('/autos/result/%s/' % q)
	return render_to_response("autos/auto3search.html", {"errors": errors, "all_users": all_users})



def show_offers_of_user(request, username):
	try:
		user = User.objects.get(username=username)
	except ObjectDoesNotExist:
		return HttpResponseRedirect("/autos/search/")

	
	alloffers = user.userToAuto3.all()
	errors = []
	content = []
	if not alloffers:
		errors.append(user.username + ' has no offers.')
	else:
		for entry in alloffers:
			if entry.is_active:
				l = []
				l.append(entry.auto_name)
				if entry.pic1:
					l.append(entry.pic1)
				if entry.pic2:
					l.append(entry.pic2)
				if entry.pic3:
					l.append(entry.pic3)
				if entry.pic4:
					l.append(entry.pic4)
				if entry.pic5:
					l.append(entry.pic5)
				content.append(tuple(l))
		if not content:
			errors.append(user.username + ' has no offers.')

#		for entry in alloffers:
#			content.append((entry.auto_name, entry.pic1, entry.pic2, entry.pic3, entry.pic4, entry.pic5))

	return render_to_response("autos/auto3result.html",
			{'errors': errors, 'content': content, 'username': user.username},
                   context_instance=RequestContext(request))
