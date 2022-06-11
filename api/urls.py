from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='apiOverview'),
    path('post-list/', views.post_list, name='posts'), 
    path('profile-list/', views.profile_list, name='profile'), 
    


]

