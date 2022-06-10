from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Posts':'/post-list/',
        'Profile': '/profile',
        'Detail_view':'/post-detail/<str:pk>/',
        'Create':'/post-create/',
        'Update':'/post-update/<str:pk>/',
        'Delete':'/post-delete/<str:pk>/',
    }
    return Response(api_urls)