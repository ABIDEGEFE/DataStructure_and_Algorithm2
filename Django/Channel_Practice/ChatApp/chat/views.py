from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    print('this is index view')
    return render(request, 'chat/login.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def login_view(request):
    print('this is login view')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print('username:', username)
        print('password:', password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)        # ← This creates sessionid cookie!
            return redirect('select_room')
        else:
            return render(request, "chat/login.html", {"error": "Bad credentials"})
    return render(request, "chat/login.html")


def logout_view(request):
    logout(request)
    return redirect('loginPage')

def select_room(request):
    return render(request, "chat/index.html")

@login_required
def chat_page(request):
    return render(request, "chat/room.html")