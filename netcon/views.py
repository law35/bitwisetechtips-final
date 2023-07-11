from django.views import generic
from .models import NetconPost
#===========================================================================================================#

class NetconPostList(generic.ListView):
	queryset = NetconPost.objects.all().order_by('-created_on')
	template_name = 'netcon.html'
	paginate_by = 5

class NetconPostDetail(generic.DetailView):
	model = NetconPost
	template_name = 'netcon_post_detail.html'
