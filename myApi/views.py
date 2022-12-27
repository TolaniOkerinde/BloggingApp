from django.shortcuts import render
from myApi import models
from .models import UserProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from myApi import serializers
from myApi import permissions
from rest_framework.authtoken.views import ObtainAuthToken 
# for login 
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings





# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class= serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    #comma to differentiate between tuple and single item
    # authentication_classes how user will be authenticated 
    # Permission classes how users will be granted permission to do certain things 

    permission_classes = (permissions.UpdateOwnProfile,)
    filters_backends = (filters.SearchFilter,)
    # for search fields 
    search_fields =('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token """

    #renderer classes is a class variable 
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ProfileFeedViewset(viewsets.ModelViewSet):
    #first authenticate
    authentication_classes =(TokenAuthentication,)
    serializer_class= serializers.ProfileFeedSerializer
    queryset= models.ProfileFeed.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)


    def perform_create(self,serializer):
        """Sets user profile to the logged in user"""

        serializers.save(UserProfile.request.user)
