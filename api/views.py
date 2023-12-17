from http.client import BAD_REQUEST
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from functools import wraps

from .models import Todo
from .serializers import TodoSerializer
from .exceptions import ValidationError
# Create your views here.

# Exception Handler Wrapper
def apiHandler(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Todo.DoesNotExist as e:
            return Response({
                    "Message": f"Todo with ID:'{kwargs.get('pk')}' is not exist", 
                    "description": str(e.__doc__),
                    "status": "404 NOT FOUND",
                    "errors": list(e.args),
                    "exception_origin": e.__class__.__name__,
                }, status=404)
            
        except ValidationError as e:
            return Response({
                    "Message": "Validation Error", 
                    "description": str(e.description),
                    "status": e.statusMessage,
                    "errors": list(e.args),
                    "exception_origin": e.__class__.__name__,
                }, status=e.statusCode)
            
        except Exception as e:
            return Response({
                    "Message": str(e), 
                    "description": str(e.__doc__),
                    "status": "500 Internal Server Error",
                    "errors": list(e.args),
                    "exception_origin": e.__class__.__name__,
                }, status=500)
    
    return wrapper
    
        
@api_view(['GET'])
@apiHandler
def apiOverview(request):
    routes = [
        'GET /api',
        'GET /api/todos',
        'POST /api/todos/create',
        'GET /api/todos/:id',
        'PUT /api/todos/:id/update',
        'DELETE /api/todos/:id/delete',
    ]
    
    data = {
        "description": "Todo API Overview",
        "routes": routes
    }
    
    return Response(data)

@api_view(['GET'])
@apiHandler
def getAllTodos(request):
    todos = TodoSerializer(Todo.objects.all(), many = True)
    data ={
        "description": "Get All Todos",
        "todos": todos.data
    }
    
    return Response(data, status=200)

@api_view(['GET'])
@apiHandler
def getTodoById(request, pk):
    todo = TodoSerializer(Todo.objects.get(id=pk))
    
    data = {
        "description": "Get a Todo By Id",
        "todo": todo.data,
    }
    
    return Response(data, status=200)

@api_view(['POST'])
@apiHandler
def createTodo(request):
    todo = TodoSerializer(data=request.data)

    if not todo.is_valid():
        raise ValidationError(todo.errors)

    todo.save()
    data = {
        "description": "Create a Todo",
        "todo": todo.data
    }
    
    return Response(data, status=201) 

@api_view(['PUT'])
@apiHandler
def updateTodo(request, pk):
    
    todo = TodoSerializer(Todo.objects.get(id=pk), data=request.data)
    if not todo.is_valid():
        raise BAD_REQUEST(todo.errors)

    todo.save()
    data = {
        "description": "Update a Todo By Id",
        "todo": todo.data
    }
    
    return Response(data, status=200)

@api_view(['DELETE'])
@apiHandler
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    serializedTodo = TodoSerializer(todo)
    todo.delete()
    
    serializedTodo = serializedTodo.data.copy()
    serializedTodo.pop('id', None)
    data = {
        "description": "Delete a Todo By Id",
        "todo": serializedTodo
    }
    
    return Response(data, status=200)

