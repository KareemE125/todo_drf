from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.exceptions import AuthenticationFailed 

from exceptionHandling.apiHandler import apiHandler
from exceptionHandling.validationExecption import ValidationException
from .serializers import UserSerializer
from .models import User
from .jwtHelpers import JWTHelper

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

    if not user.check_password(password):
        raise AuthenticationFailed("Wrong Password")
    
    serializedUser = UserSerializer(user)

    data = {
        "description": "Login a User",
        "token": JWTHelper.encode(user.getJson()),
        "user": serializedUser.data
    }
    
    return Response(data, status=200)

