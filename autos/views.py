# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from firstsite.autos.forms import *
from firstsite.autos.models import *
from django.contrib.auth.decorators import user_passes_test, login_required




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
	
	return render_to_response("autos/auto3result.html",
			{'errors': errors, 'content': content, 'username': user.username},
                   context_instance=RequestContext(request))


#needs to be login for using /autos/addcar
@user_passes_test(lambda u: u.has_perm('autos.add_auto3'))
def add_a_car(request):
	if request.method == 'POST':
		form = Auto3Form(request.POST, request.FILES)
		if form.is_valid():
			car = form.save(commit=False)
			car.user = request.user
			car.save()
			return HttpResponseRedirect('/autos/result/%s/' % request.user.username)
	else:
		form = Auto3Form()
	
	return render_to_response('autos/add_a_car.html', {'form': form, 'user': request.user})


#needs to be login for using /autos/showcars
@login_required
def list_cars_for_editing(request):
	car_list = Auto3.objects.filter(user=request.user.id)

	errors = []
	if not car_list:
		errors.append((request.user.username + u' hat keine Einträge.'))

	return render_to_response('autos/carlist_of_user.html', {
			'errors': errors,
			'car_list': car_list,
			'user': request.user,
		})

