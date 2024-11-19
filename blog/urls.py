from django.urls import path
from . import views


# a list that lists all the urls that we will make point to html pages/views
# it is contained in a list called urlpatterns

urlpatterns = [
    #index or homepage
    path('', views.post_list, name='post_list')
]