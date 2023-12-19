from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 

from execptionHandling.apiHandler import apiHandler
from execptionHandling.validationExecption import ValidationException
from .serializers import UserSerializer
from.models import User
# Create your views here.

@api_view(['POST'])
@apiHandler
def signup(request):
    user = UserSerializer(data=request.data)
    if not user.is_valid():
        raise ValidationException(user.errors)
    
    user.save()

    data = {
        "description": "Signup a User",
        "user": user.data
    }
    
    return Response(data, status=201) 


@api_view(['POST'])
@apiHandler
def login(request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    user = User.objects.get(email=email)
    print(password)
    print(user.check_password(password))
    if not user.check_password(password):
        raise ValidationException("Wrong Password")
    
    user = UserSerializer(user)
    
    data = {
        "description": "Login a User",
        "user": user.data
    }
    
    return Response(data, status=200)

