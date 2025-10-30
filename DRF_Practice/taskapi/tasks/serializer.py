from rest_framework import serializers
from django.contrib.auth.models import User, Group
from . models import Task, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'full_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    def get_is_overdue(self, obj):
        from django.utils import timezone
        if obj.due_date:
            return obj.due_date < timezone.now()
        return False
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or whitespace.")
        return value
    
    owner = UserSerializer(read_only=False)
    category = CategorySerializer(read_only=False)
    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'owner', 'category', 'due_date', 'status', 'is_overdue']
