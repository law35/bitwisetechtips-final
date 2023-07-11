from django.shortcuts import render
#from django.template.context import RequestContext

# Create your views here.
def index(request):
	return render(request, 'home.html')