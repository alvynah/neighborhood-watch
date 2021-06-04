from django.shortcuts import render,HttpResponse
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class  NeighborhoodList(APIView):
    def get(self,request,format=None):
       neighborhood=Neighborhood.objects.all()
       serializers=NeighborhoodSerializer(neighborhood,many=True)
       return Response(serializers.data) 