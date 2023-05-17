from django.shortcuts import render
from .models import ChatMessage

def index(request):
    return render(request, 'chatapp/index.html')

def roomName(request, room_name):
    chat_messages = ChatMessage.objects.all()
    return render(request, 'chatapp/chatroom.html', {'room_name': room_name, 'chat_messages': chat_messages})
