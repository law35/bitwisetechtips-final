from django.views import generic
from .models import PythonPost
#===========================================================================================================#

class PythonPostList(generic.ListView):
	queryset = PythonPost.objects.all().order_by('-created_on')
	template_name = 'python.html'
	paginate_by = 5

class PythonPostDetail(generic.DetailView):
	model = PythonPost
	template_name = 'python_post_detail.html'
