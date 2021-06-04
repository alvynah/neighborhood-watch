from django.shortcuts import render,HttpResponse
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class  NeighborhoodList(APIView):
    def get_neighborhood(self, pk):
        try:
            return Neighborhood.objects.get(pk=pk)
        except Neighborhood.DoesNotExist:
            return Http404 
    def get(self,request,format=None):
       neighborhood=Neighborhood.objects.all()
       serializers=NeighborhoodSerializer(neighborhood,many=True)
       return Response(serializers.data)

    def post(self,request,format=None):
        serializers=NeighborhoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            neighborhood=serializers.data
            response={
                'data':{
                    'neighborhood':dict(neighborhood),
                    'status':'success',
                    'message':'neighborhood created successfully',
                }
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        serializers = NeighborhoodSerializer(neighborhood, request.data)
        if serializers.is_valid():
            serializers.save()
            neighborhood=serializers.data
            response = {
                     'data': {
                     'neighborhood': dict(neighborhood),
                     'status': 'success',
                    'message': 'neighborhood updated successfully',
                 }
             }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        neighborhood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)