from . import views
from django.urls import path
#====================================================================================================#

urlpatterns = [
    path('netcon', views.NetconPostList.as_view(), name='netcon'),
    path('netcon/<slug:slug>/', views.NetconPostDetail.as_view(), name='netcon_post_detail'),
]