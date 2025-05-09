from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import ChatRoom, Message
from .forms import ChatRoomForm, MessageForm

@login_required
def chatroom_list(request):
    chatrooms = request.user.chatrooms.all()
    return render(request, 'communication/chatroom_list.html', {'chatrooms': chatrooms})

@login_required
def chatroom_create(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chatroom = form.save(commit=False)
            chatroom.creator = request.user
            chatroom.save()
            form.save_m2m()
            chatroom.members.add(request.user)  # Add creator to members
            return redirect(reverse('communication:chatroom_detail', args=[chatroom.id]))
    else:
        form = ChatRoomForm()
    return render(request, 'communication/chatroom_form.html', {'form': form})

@login_required
def chatroom_detail(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
    if request.user not in chatroom.members.all():
        return redirect('communication:chatroom_list')
    messages = chatroom.messages.order_by('timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chatroom = chatroom
            message.sender = request.user
            message.save()
            return redirect(reverse('communication:chatroom_detail', args=[chatroom.id]))
    else:
        form = MessageForm()
    return render(request, 'communication/chatroom_detail.html', {'chatroom': chatroom, 'messages': messages, 'form': form})
