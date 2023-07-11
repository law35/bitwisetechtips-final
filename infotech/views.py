from django.views import generic
from .models import ITPost
#==============================================================================#

class ITPostList(generic.ListView):
	queryset = ITPost.objects.all().order_by('-created_on')
	template_name = 'infotech.html'
	paginate_by = 5

class ITPostDetail(generic.DetailView):
	model = ITPost
	template_name = 'it_post_detail.html'