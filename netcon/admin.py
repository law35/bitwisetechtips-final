from django.contrib import admin
from .models import NetconPost, Image
#===============================================================================#

class NetconPostAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'author',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = NetconPost
#===============================================================================#

class NetconImageAdmin(admin.ModelAdmin):
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

admin.site.register(NetconPost, NetconPostAdmin)
admin.site.register(Image, NetconImageAdmin)