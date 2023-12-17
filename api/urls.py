from django.urls import path
from . import views 

urlpatterns = [
    path('', views.apiOverview),
    path('todos', views.getAllTodos),
    path('todos/create', views.createTodo),
    path('todos/<str:pk>', views.getTodoById),
    path('todos/<str:pk>/update', views.updateTodo),
    path('todos/<str:pk>/delete', views.deleteTodo),
]
