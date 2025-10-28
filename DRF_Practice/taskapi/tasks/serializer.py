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

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # def check_due_date(value):
    #     from datetime import date
    #     if value < date.today():
    #         raise serializers.ValidationError("Due date cannot be in the past.")
    #     return value
    
    owner = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all(),
        read_only=False
    )
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        queryset=Category.objects.all(),
        read_only=False,
        allow_null=True
    )
    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'owner', 'category', 'due_date', 'status']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description']
