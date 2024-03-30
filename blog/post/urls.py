from django.urls import path

from post.views import post_list

urlpatterns = [
	path('list/', post_list, name='post_list'),
]
