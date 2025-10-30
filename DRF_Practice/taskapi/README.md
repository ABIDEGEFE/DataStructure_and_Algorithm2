# **Django REST Framework (DRF) Task API – Learning Project**

![Django](https://img.shields.io/badge/Django-5.x-green) ![DRF](https://img.shields.io/badge/DRF-3.x-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

A **step-by-step learning journey** into building a **RESTful Task Management API** using **Django** and **Django REST Framework (DRF)**. This project demonstrates core API design principles, best practices, and real-world patterns.

---

## Project Structure

```
taskapi/
├── taskapi/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
└── manage.py
```

---

Flow of the request: 

<img width="611" height="191" alt="FlowDiagram" src="https://github.com/user-attachments/assets/d853d09e-c1ef-47a8-8786-6c9abf45f2bc" />


## Step 1: Environment Setup

```bash
# Create virtual environment
python -m venv drfPractice
source drfPractice/bin/activate  # On Windows: drfPractice\Scripts\activate

# Install dependencies
pip install django djangorestframework

# Start Django project
django-admin startproject taskapi
cd taskapi

# Create tasks app
python manage.py startapp tasks
```

### Update `taskapi/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tasks',
]
```

### Initial Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Step 2: Model Design

Models define the database schema. Each model maps to a database table.

### `tasks/models.py`

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['owner']),
        ]

    def __str__(self):
        return self.title
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Register in Admin (`tasks/admin.py`)

```python
from django.contrib import admin
from .models import Task, Category

admin.site.register(Task)
admin.site.register(Category)
```

---

## Step 3: Serializers

Serializers convert complex Python objects (e.g., model instances) to JSON and validate incoming data.

### `tasks/serializers.py`

```python
from rest_framework import serializers
from django.utils import timezone
from .models import Task, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description', 'created_at']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    is_overdue = serializers.SerializerMethodField()
    owner = UserSerializer(read_only=False)
    category = CategorySerializer(read_only=False)

    class Meta:
        model = Task
        fields = [
            'url', 'title', 'description', 'status', 'owner',
            'category', 'created_at', 'updated_at', 'due_date', 'is_overdue'
        ]

    def get_is_overdue(self, obj):
        if obj.due_date:
            return obj.due_date < timezone.now()
        return False

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or whitespace.")
        return value
```

> **Note**: `HyperlinkedModelSerializer` is ideal for public APIs. Use `ModelSerializer` + `PrimaryKeyRelatedField` for internal APIs.

---

## Step 4: ViewSets

ViewSets group logic for multiple HTTP methods (CRUD) into a single class.

### `tasks/views.py`

```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'COMPLETED'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
```

> **Key Concepts**:
> - `queryset`: Base query for the model
> - `serializer_class`: Links to serializer
> - `permission_classes`: Enforces authentication
> - `get_queryset()`: Filters tasks per user
> - `@action`: Creates custom endpoint (`/tasks/{id}/mark-complete/`)

---

## Step 5: URL Routing

DRF routers automatically generate RESTful URLs.

### `taskapi/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

### Generated Endpoints

| Method | URL | Action |
|-------|-----|--------|
| `GET` | `/tasks/` | List user tasks |
| `POST` | `/tasks/` | Create task |
| `GET` | `/tasks/1/` | Retrieve task |
| `PUT/PATCH` | `/tasks/1/` | Update task |
| `DELETE` | `/tasks/1/` | Delete task |
| `POST` | `/tasks/1/mark-complete/` | Mark as complete |

---

## Testing the API

1. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

2. **Run server**
   ```bash
   python manage.py runserver
   ```

3. **Browse API**
   - Root: `http://127.0.0.1:8000/`
   - Tasks: `http://127.0.0.1:8000/tasks/`
   - Login: `http://127.0.0.1:8000/api-auth/login/`

4. **Test Custom Action**
   - `POST /tasks/1/mark-complete/` → Sets status to `COMPLETED`

---

## Key Learnings

| Concept | Implementation |
|-------|----------------|
| **Virtual Environment** | Isolated dependencies |
| **Model Design** | Relational DB with indexes |
| **Serializers** | Validation + computed fields |
| **ViewSets** | DRY CRUD logic |
| **Custom Actions** | `@action` + router |
| **Authentication** | `IsAuthenticated` + session |
| **Browsable API** | Built-in testing UI |


---

> **"The best way to learn is to build."**  
> This project is a living documentation of mastering DRF from zero to production-ready API.

---

**Star this repo if you found it helpful!**  
Feel free to fork, contribute, or use as a template for your next API project.

