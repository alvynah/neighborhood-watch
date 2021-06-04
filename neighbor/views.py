from django.shortcuts import render,HttpResponse

# Create your views here.

def welcome(reguest):
   return HttpResponse("Wow")