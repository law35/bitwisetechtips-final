from django.contrib import admin
from .models import ITPost, ITImage
#===============================================================================#

class ITPostAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'author',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}
	
	class Meta:
		model = ITPost
#===============================================================================#

class ITImageAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'uploader',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}
	
	class Meta:
		model = ITImage
#===============================================================================#

admin.site.register(ITPost, ITPostAdmin)
admin.site.register(ITImage, ITImageAdmin)