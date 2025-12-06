from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('select_room/', views.select_room, name='select_room'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('<str:room_name>/', views.room, name='room'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]