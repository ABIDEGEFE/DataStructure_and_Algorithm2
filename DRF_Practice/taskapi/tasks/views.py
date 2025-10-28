from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Task, Category
from .serializer import UserSerializer, GroupSerializer, TaskSerializer, CategorySerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    print('User Queryset:', queryset)
    serializer_class = UserSerializer
    print('User Serializer class:', serializer_class)
    permission_classes = [permissions.AllowAny]


    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        user = self.get_object()
        print('Fetching profile for user:', user)
        return Response({'username': user.username, 'email': user.email})
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     print('Filtering tasks for user:', self.request.user)
    #     return super().get_queryset().filter(owner=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        print('Marking task as complete:', pk)
        task = self.get_object()
        task.status = 'completed'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
        

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]