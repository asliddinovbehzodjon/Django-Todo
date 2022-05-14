from django.shortcuts import render

# Create your views here.
from .serializer import TodoSerializer
from .models import Todo
from  rest_framework import viewsets
class TodoAll(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
