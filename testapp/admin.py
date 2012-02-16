from django.contrib import admin
from firstsite.testapp.models import *


class AutoAdmin(admin.ModelAdmin):
	list_display = ('name', 'marke', 'preis', 'user')
	search_fields = ('name', 'preis')

	def queryset(self, request):
		qs = super(AutoAdmin, self).queryset(request)
		if not request.user.is_superuser:
			qs = qs.filter(user=request.user)
		return qs

admin.site.register(Auto, AutoAdmin)