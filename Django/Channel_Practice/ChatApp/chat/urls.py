from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('select_room/', views.select_room, name='select_room'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:room_name>/', views.room, name='room'),
]