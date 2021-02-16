from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def room(reques, room_name):
    return render(request, 'chatroom.html', {
        'room name': room_name
    })