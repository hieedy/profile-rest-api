from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profile_api import serializers
from profile_api import models
from profile_api import permissions

#there are two wasy to create view using django rest rest_framework
#using APIView and second ViewSet
#Lets see the example for those.


# Create your views here.
# in APIView we add function for
# particular http methods that you wanna support for your
#end point. ex : http post, http get, http patch ,etc
class HelloApiView(APIView):
    """Creating simple APIView for texting"""
    serializer_class   = serializers.HelloSerializer


    def get(self, request, format=None):
        """return an list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional DJango View',
        'Gives you the  most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Heloo!','features':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )


    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method':'PUT'})


    def patch(self, request, pk = None):
        """Handle a partial update of an object """
        return Response({'method':'PATCH'})


    def delete(self, request, pk = None):
        """Delete an object """

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APIVIew Set """
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello messagee"""
        a_viewset = [
        'Uses actions (list, create , retrieve, update, partial_model)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':"HEllo!!", 'a_viewset':a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
            )


    #used to retrieve specific object so need to pass primary key
    # maps to our http get request
    def retrieve(self, request, pk=None):
        """Handle getting anbyt its ID """

        return Response({'http_method':'GET'})


    #maps to our http put request
    def update(self, request, pk = None):
        """Handle updating an object """
        return Response({'http_method': 'PUT'})

    #Maps to our http patch request
    def partial_update(self, request, pk = None):
        """Handle updating part of an object """
        return Response({'http_method':'PATCH'})

    #Maps to http delete request
    def destroy(self, request, pk =None):
        "Handle removing an object"
        return Response({'http_method':'DELETE'})



# using ModelViewSet
class  UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter, )
    search_fields = ('name','email')

class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
