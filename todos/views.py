from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer
from .models import Todo

class TodoList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        todos = Todo.objects.filter(user=request.user).filter(deleted=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        # Comentado para pruebas, originalmente busca que coincida tambien el usuario
        # todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        # Comentado para pruebas, originalmente busca que coincida tambien el usuario
        # todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)