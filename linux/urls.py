from . import views
from django.urls import path
#===============================================================================#

urlpatterns = [
    path('linux', views.LinuxPostList.as_view(), name='linux'),
    path('linux/<slug:slug>/', views.LinuxPostDetail.as_view(), name='linux_post_detail'),
]