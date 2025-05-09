import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import ChatRoom, Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        self.chatroom_group_name = f'chat_{self.chatroom_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.chatroom_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chatroom_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get('type', 'message')
        sender_id = self.scope['user'].id

        if event_type == 'message':
            message = data['message']
            # Save message to database
            msg = await self.save_message(sender_id, self.chatroom_id, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender_id': sender_id,
                    'sender_name': self.scope['user'].get_full_name(),
                    'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                }
            )
        elif event_type == 'typing':
            is_typing = data['is_typing']
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'typing',
                    'sender_id': sender_id,
                    'sender_name': self.scope['user'].get_full_name(),
                    'is_typing': is_typing,
                }
            )
        elif event_type == 'read_receipt':
            message_id = data['message_id']
            await self.mark_message_read(sender_id, message_id)
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'read_receipt',
                    'sender_id': sender_id,
                    'message_id': message_id,
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']
        sender_name = event['sender_name']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message,
            'sender_id': sender_id,
            'sender_name': sender_name,
            'timestamp': timestamp,
        }))

    async def typing(self, event):
        sender_id = event['sender_id']
        sender_name = event['sender_name']
        is_typing = event['is_typing']

        await self.send(text_data=json.dumps({
            'type': 'typing',
            'sender_id': sender_id,
            'sender_name': sender_name,
            'is_typing': is_typing,
        }))

    async def read_receipt(self, event):
        sender_id = event['sender_id']
        message_id = event['message_id']

        await self.send(text_data=json.dumps({
            'type': 'read_receipt',
            'sender_id': sender_id,
            'message_id': message_id,
        }))

    @database_sync_to_async
    def save_message(self, sender_id, chatroom_id, message):
        sender = User.objects.get(id=sender_id)
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        return Message.objects.create(chatroom=chatroom, sender=sender, content=message)

    @database_sync_to_async
    def mark_message_read(self, user_id, message_id):
        try:
            message = Message.objects.get(id=message_id)
            # Mark message as read for the user (extend model if needed)
            message.is_read = True
            message.save()
        except Message.DoesNotExist:
            pass
