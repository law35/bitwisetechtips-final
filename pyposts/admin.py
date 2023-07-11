from django.contrib import admin
from .models import PythonPost, Image
#===============================================================================#

class PythonPostAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'author',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = PythonPost
#===============================================================================#

class PythonImageAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'uploader',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = Image
#===============================================================================#

admin.site.register(PythonPost, PythonPostAdmin)
admin.site.register(Image, PythonImageAdmin)