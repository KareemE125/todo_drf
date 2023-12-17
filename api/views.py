from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    routes = [
        'GET /api',
        'GET /api/todos',
        'GET /api/todo/<str:pk>',
        'POST /api/todo-create',
        'POST /api/todo-update/<str:pk>',
        'DELETE /api/todo-delete/<str:pk>',
    ]
    
    data = {
        "description": "Todo API Overview",
        "routes": routes
    }
    
    return Response(data)

@api_view(['GET'])
def getAllTodos(request):
    todos = TodoSerializer(Todo.objects.all(), many = True)
    data ={
        "description": "Get All Todos",
        "todos": todos.data
    }
    
    return Response(data)







