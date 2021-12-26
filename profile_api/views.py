from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Creating simple APIView for texting"""


    def get(self, request, format=None):
        """return an list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional DJango View',
        'Gives you the  most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Heloo!','features':an_apiview})
