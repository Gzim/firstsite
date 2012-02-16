from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=50, blank=True)
	state_province = models.CharField(max_length=60, blank=True)
	country = models.CharField(max_length=50, blank=True)
	website = models.URLField(blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True)

	def _get_everything(self):
		return u'%s %s %s' % (self.first_name, self.last_name, self.email)

	everything = property(_get_everything)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)


class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

class KisteBookManager(models.Manager):
	def get_query_set(self):
		return super(KisteBookManager, self).get_query_set().filter(authors="2")

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(null=True, blank=True)
	objects = models.Manager() #The default manager.
	book_objects = BookManager()
	kiste_objects = KisteBookManager()

	def __unicode__(self):
		return self.title