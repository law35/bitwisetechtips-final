from . import views
from django.urls import path
#====================================================================================================#

urlpatterns = [
    path('python', views.PythonPostList.as_view(), name='python'),
    path('python/<slug:slug>/', views.PythonPostDetail.as_view(), name='python_post_detail'),
]