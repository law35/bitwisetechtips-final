from django.views import generic
from .models import LinuxPosts
#==============================================================================#

class LinuxPostList(generic.ListView):
	queryset = LinuxPosts.objects.all().order_by('-created_on')
	template_name = 'linux.html'
	paginate_by = 5

class LinuxPostDetail(generic.DetailView):
	model = LinuxPosts
	template_name = 'linux_post_detail.html'