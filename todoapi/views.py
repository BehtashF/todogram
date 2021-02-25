from django.shortcuts import get_object_or_404
from todo.models import Task
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # def list(self, request):
    #     queryset = Task.objects.all()
    #     serializer = TaskSerializer(queryset , many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Task.objects.all()
    #     task = get_object_or_404(queryset, pk=pk)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     serializer = TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'ok'})
    #     else:
    #         return Response(serializer.errors)
        
    # def update(self, request, pk=None, *args, **kwargs):
    #     partial = True
    #     queryset = Task.objects.all()
    #     task = get_object_or_404(queryset, pk=pk)
    #     serializer = TaskSerializer(instance=task, data=request.data , partial=partial)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'task update successfully'})
    #     else:
    #         return Response(serializer.errors)
    
    
    # def destroy(self, request, pk=None):
    #     queryset = Task.objects.all()
    #     task = get_object_or_404(queryset, pk=pk)
    #     task.delete()
    #     return Response({'message' : 'Task deleted successfully'})
    