from django.urls import path
from . import views 

urlpatterns = [
    path('', views.apiOverview),
    path('todos', views.getAllTodos),
    path('todos/<str:pk>', views.getTodoById),
]
