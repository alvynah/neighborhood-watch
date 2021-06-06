from rest_framework import serializers
from .models import *
from django import forms


#serializer classes

class BusinessSerializer(serializers.ModelSerializer):
   class Meta:
        model = Business
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    business=BusinessSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = "__all__"
        
class NeighborhoodSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=True, read_only=True)
    business = BusinessSerializer(many=True, read_only=True)

    class Meta:
        model = Neighborhood
        fields = "__all__"
 
