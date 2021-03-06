from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.api_overview, name='apiOverview'),
    path('post-list/', views.post_list, name='posts'), 
    path('profile-list/', views.profile_list, name='profile'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
