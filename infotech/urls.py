from . import views
from django.urls import path
#===============================================================================#

urlpatterns = [
    path('InfoTech', views.ITPostList.as_view(), name='infotech'),
    path('infotech/<slug:slug>/', views.ITPostDetail.as_view(), name='it_post_detail'),
]