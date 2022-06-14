from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'), 
    path('signup/', views.register_user, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<str:pk>', views.update_profile, name='update-profile'),
    path('project/<post>/', views.project, name='project'),
    path('submit/', views.add_post, name='submit'),
    path('search/', views.search, name='search'),
]