from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializer import UserSerializer, GroupSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    print('User Queryset:', queryset)
    serializer_class = UserSerializer
    print('User Serializer class:', serializer_class)
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        user = self.get_object()
        print('Fetching profile for user:', user)
        return Response({'username': user.username, 'email': user.email})
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]