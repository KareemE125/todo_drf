from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
# Create your views here.

# def apiHandler(func):
    
#     def wrapper(request, *args, **kwargs):
#         try:
            
#         except Exception as e:
            
    
#     return wrapper
    

@api_view(['POST'])
def login(request):
    
    return Response()

@api_view(['POST'])
def signup(request):
    
    return Response()