from django.contrib import admin
from firstsite.autos.models import *


class Auto1Admin(admin.ModelAdmin):
	list_display = ('auto_name', 'owner')

	def has_change_permission(self, request, obj=None):
		has_class_permission = super(Auto1Admin, self).has_change_permission(request, obj)
		if not has_class_permission:
			return False
		if obj is not None and not request.user.is_superuser and request.user.id != obj.owner.id:
			return False
		return True


	def queryset(self, request):
		if request.user.is_superuser:
			return Auto1.objects.all()
		return Auto1.objects.filter(owner=request.user)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.owner = request.user
		obj.save()

class Auto2Admin(admin.ModelAdmin):
	list_display = ('auto_name', 'user_name')

	def has_change_permission(self, request, obj=None):
		has_class_permission = super(Auto2Admin, self).has_change_permission(request, obj)
		if not has_class_permission:
			return False
		if obj is not None and not request.user.is_superuser and request.user.id != obj.user_name.id:
			return False
		return True


	def queryset(self, request):
		if request.user.is_superuser:
			return Auto2.objects.all()
		return Auto2.objects.filter(user_name=request.user)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.user_name = request.user
		obj.save()


class AutoDesAuthorsAdmin(admin.ModelAdmin):
	list_display = ('auto_name', 'belongs_to')



class ImageInline(generic.GenericTabularInline):
	model = Image


class Auto3Admin(admin.ModelAdmin):
	list_display = ('auto_name', 'firstname', 'lastname', 'belongs_to', 'is_active', 'paste_on_date',  'user')

	fieldsets = [
		(None,			{'fields': ['auto_name', 'firstname', 'lastname', 'belongs_to']}),
		("Bild(er)",	{'fields': ['pic1', 'pic2', 'pic3', 'pic4', 'pic5'], 'classes': ['collapse']}),
		("Aktivierung",	{'fields': ['is_active',]}),
	]
	#inlines = [ImageInline]


	def has_change_permission(self, request, obj=None):
		has_class_permission = super(Auto3Admin, self).has_change_permission(request, obj)
		if not has_class_permission:
			return False
		if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
			return False
		return True


	def queryset(self, request):
		if request.user.is_superuser:
			return Auto3.objects.all()
		return Auto3.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
		obj.save()

admin.site.register(Auto1, Auto1Admin)
admin.site.register(Auto2, Auto2Admin)
admin.site.register(AutoDesAuthors, AutoDesAuthorsAdmin)
admin.site.register(Auto3, Auto3Admin)










