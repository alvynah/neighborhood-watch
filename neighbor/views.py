from django.contrib.auth.models import Permission
from django.shortcuts import render,HttpResponse
from django.http import Http404
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import IsAdminOrReadOnly

# Create your views here.

class  NeighborhoodList(generics.ListCreateAPIView):
    def get_neighborhood(self, pk):
        try:
            return Neighborhood.objects.get(pk=pk)
        except Neighborhood.DoesNotExist:
            return Http404 
   
    def get(self,request,pk,format=None):
        neighborhood=self.get_neighborhood(pk)
        serializers=NeighborhoodSerializer(neighborhood)
        return Response(serializers.data)

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

class NeighborhoodPostList(generics.ListCreateAPIView):

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


class NeighborhoodDetailList(APIView):
   def get(self,request,format=None):
       neighborhood=Neighborhood.objects.all()
       serializers=NeighborhoodSerializer(neighborhood,many=True)
       return Response(serializers.data)

class NeighborhoodSearchList(APIView):
    def get(self,request,name):
        neighborhood=Neighborhood.find_neighborhood(name)
        serializers=NeighborhoodSerializer(neighborhood, many=True)
        return Response(serializers.data)
 

class BusinessList(generics.ListCreateAPIView):
        def get_business(self, pk):
            try:
                return Business.objects.get(pk=pk)
            except Business.DoesNotExist:
                return Http404()

        def get(self,request,pk,format=None):
            business=self.get_business(pk)
            serializers=BusinessSerializer(business)
            return Response(serializers.data)


        
        def put(self, request, pk, format=None):
            business = self.get_business(pk)
            serializers = BusinessSerializer(business, request.data)
            if serializers.is_valid():
                serializers.save()
                business_list=serializers.data
                response = {
                            'data': {
                            'business': dict(business_list),
                            'status': 'success',
                            'message': 'business updated successfully',
                            }
                         }
                return Response(response)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            business = self.get_business(pk)
            business.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessPostList(generics.ListCreateAPIView):
    def post(self, request, format=None):
            serializers=BusinessSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                business=serializers.data
                response = {
                            'data': {
                            'business': dict(business),
                            'status': 'success',
                            'message': 'business created successfully',
                         }
                     }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessDetailList(APIView):
       def get(self,request,format=None):
        business=Business.objects.all()
        serializers=BusinessSerializer(business,many=True)
        return Response(serializers.data)

class BusinessSearchList(APIView):
    def get(self,request,name):
        business=Business.find_business(name)
        serializers=BusinessSerializer(business, many=True)
        return Response(serializers.data)
    



class ProfileList(generics.ListCreateAPIView):
    def get_profile(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404()
    
    
    def get(self,request,pk,format=None):
        profiles=self.get_profile(pk)
        serializers=ProfileSerializer(profiles)
        return Response(serializers.data)

    def put(self,request,pk,format=None):
        profiles=self.get_profile(pk)
        serializers=ProfileSerializer(profiles,request.data)
        if serializers.is_valid():
            serializers.save()
            profiles_list=serializers.data
            response = {
                        'data': {
                        'users': dict(profiles_list),
                        'status': 'success',
                        }
                     }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailsList(APIView):
    def get(self,request,format=None):
        profiles=Profile.objects.all()
        serializers=ProfileSerializer(profiles,many=True)
        return Response(serializers.data)

class ProfileSearchList(APIView):
    def get(self,request,search_term):
        profiles=Profile.search_profile(search_term)
        serializers=ProfileSerializer(profiles, many=True)
        return Response(serializers.data)  



class UserList(generics.ListCreateAPIView):
    def get_users(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404()
    
    
    def get(self,request,pk,format=None):
            business=self.get_users(pk)
            serializers=UserSerializer(business)
            return Response(serializers.data)
    
        
    def delete(self,request,pk,format=None):
        users=self.get_users(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserPostList(generics.ListCreateAPIView):
    def post(self, request, format=None):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()

            users=serializers.data
            response={
                        'data':{
                        'users':dict(users),
                        'status':'success',
                        'message':'user created successfully',
                     }
                }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
 

class UserDetailList(APIView):
       def get(self,request,format=None):
        users=User.objects.all()
        serializers=UserSerializer(users,many=True)
        return Response(serializers.data)

class UserSearchList(APIView):
    def get(self,request,name):
        users=User.find_user(name)
        serializers=UserSerializer(users, many=True)
        return Response(serializers.data)


class  PostList(generics.ListCreateAPIView):
    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404 
   
    def get(self,request,pk,format=None):
        posts=self.get_post(pk)
        serializers=PostSerializer(posts)
        return Response(serializers.data)


   

    def put(self, request, pk, format=None):
        posts = self.get_post(pk)
        serializers = PostSerializer(posts, request.data)
        if serializers.is_valid():
            serializers.save()
            posts=serializers.data
            response = {
                     'data': {
                     'posts': dict(posts),
                     'status': 'success',
                    'message': 'posts updated successfully',
                 }
             }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        posts = self.get_post(pk)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PostPostList(generics.ListCreateAPIView):
     def post(self,request,format=None):
        serializers=PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            posts=serializers.data
            response={
                'data':{
                    'posts':dict(posts),
                    'status':'success',
                    'message':'posts created successfully',
                }
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailList(APIView):
   def get(self,request,format=None):
       posts=Post.objects.all()
       serializers=PostSerializer(posts,many=True)
       return Response(serializers.data)

class PostSearchList(APIView):
    def get(self,request,name):
        posts=Post.search_post(name)
        serializers=PostSerializer(posts, many=True)
        return Response(serializers.data)

 
def index(request):
    """
    The home page. This renders the container for the single-page app.
    """
    return render(request, 'base.html') 

    