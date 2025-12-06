from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    print('this is index view')
    return render(request, 'chat/login.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def select_room(request):
    return render(request, "chat/index.html")

@login_required
def chat_page(request):
    return render(request, "chat/room.html")