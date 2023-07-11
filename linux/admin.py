from django.contrib import admin
from .models import LinuxPosts, LinuxImage
#===============================================================================#

class LinuxPostsAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'author',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = LinuxPosts
#===============================================================================#

class LinuxImageAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'uploader',
		'updated', 'created_on',
	]
	list_display_links = ['title']
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = LinuxImage
#===============================================================================#

admin.site.register(LinuxPosts, LinuxPostsAdmin)
admin.site.register(LinuxImage, LinuxImageAdmin)