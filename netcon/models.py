from django.db import models
#from django.urls import reverse
#from django.utils.text import slugify
from django.conf import settings
from ckeditor.fields import RichTextField
#==============================================================================================================#

class NetconPost(models.Model):
	title = models.CharField(max_length=200, unique=True)
	thumb = models.ImageField(
					upload_to='netcon/thumbnails',
					null=True, blank=True
					)
	author = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				blank=True, null=True,
				on_delete=models.CASCADE
				)
	updated = models.DateTimeField(auto_now= True)
	description = RichTextField(blank=False, null=True)
	content = RichTextField(blank=False, null=False)
	created_on = models.DateTimeField(auto_now_add=True)
	metakeywords = RichTextField(blank=False, null=True)
	slug = models.SlugField(max_length=200, unique=True)
	file = models.FileField(
					upload_to='netcon/files',
					null=True, blank=True
					)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
#===============================================================================================================#

class Image(models.Model):
	title = models.CharField(max_length=200, unique=True)
	thumb = models.ImageField(
					upload_to='netcon/images',
					null=True, blank=True
					)
	uploader = models.ForeignKey(
				settings.AUTH_USER_MODEL,
				blank=True, null=True,
				related_name='uplodedby',
				on_delete=models.CASCADE
				)
	updated = models.DateTimeField(auto_now= True)
	created_on = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title