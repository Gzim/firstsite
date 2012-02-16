# -*- coding: utf-8 -*-
import os
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from firstsite.books.models import Author
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic




class Auto1(models.Model):
	owner = models.ForeignKey(User, related_name='owner', editable=False)
	auto_name = models.CharField(max_length=30)



class Auto2(models.Model):

	user_name = models.ForeignKey(User, related_name='user')
	auto_name = models.CharField(max_length=30)
	pic = models.ImageField(upload_to="images/", blank=True, help_text="Should bi less 2.5MB")



class AutoDesAuthors(models.Model):
	auto_name = models.CharField(max_length=40)
	belongs_to = models.ForeignKey(Author)


#get_image_path is the callable (in this case a function).
#It simply gets the id from the instance of Photo and uses that in the upload path.
def get_image_path(instance, filename):
	def removeNonAscii(s):
		return "".join(i for i in s if ord(i)<128)
	today = date.today()
	day = today.day
	month = today.month
	year = today.year
	thema = instance.auto_name.encode('ascii', 'ignore').strip().replace(' ', '.')
	return os.path.join('images', str(year), str(month), str(day), str(instance.user.username), thema, filename)
	

#this class can add multiple pictures to a car
class Auto3(models.Model):
	user = models.ForeignKey(User, related_name='userToAuto3')
	firstname = models.CharField(max_length=30, blank=True)
	lastname = models.CharField(max_length=30, blank=True)
	auto_name = models.CharField(max_length=40)
	belongs_to = models.ForeignKey(Author, verbose_name='Besitzer')
	pic1 = models.ImageField(upload_to=get_image_path, blank=True, verbose_name='Bild 1')
	pic2 = models.ImageField(upload_to=get_image_path, blank=True, verbose_name='Bild 2')
	pic3 = models.ImageField(upload_to=get_image_path, blank=True, verbose_name='Bild 3')
	pic4 = models.ImageField(upload_to=get_image_path, blank=True, verbose_name='Bild 4')
	pic5 = models.ImageField(upload_to=get_image_path, blank=True, verbose_name='Bild 5')
	paste_on_date = models.DateField(auto_now_add=True, verbose_name="Erstellt am")
	is_active = models.BooleanField(default=False, verbose_name="Ist aktiviert")

	def __unicode__(self):
		return self.auto_name

	def save(self):
		from PIL import Image
		super(Auto3, self).save()
		#import pdb; pdb.set_trace()
		pics = [self.pic1, self.pic2, self.pic3, self.pic4, self.pic5]
		for pic in pics:
			if not pic:
				continue

			img = Image.open(pic)
			(width, height) = img.size

			#Max width and height 200
			if (width < 200 or height < 200):
				if (float(200) / width < float(200) / height):
					factor = float(200) / width
				else:
					factor = float(200) / height
				size = (int(width * factor), int(height * factor))
			else:
				if (float(200) / width < float(200) / height):
					factor = float(200) / width
				else:
					factor = float(200) / height
				size = (int(width * factor), int(height * factor))

			img = img.resize(size, Image.ANTIALIAS)
			img.save(pic.path)







#Imageclass for the Other classes
class Image(models.Model):
	image = models.ImageField(upload_to=get_image_path, blank=True)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')

















