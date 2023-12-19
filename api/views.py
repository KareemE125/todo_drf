from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
from exceptionHandling.validationExecption import ValidationException
from exceptionHandling.apiHandler import apiHandler
# Create your views here.

# Exception Handler Wrapper

    
        
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
        raise ValidationException(todo.errors)

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
        raise ValidationException(todo.errors)

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

