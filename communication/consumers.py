import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import ChatRoom, Message, Reaction, MessageReadStatus, UserPresence

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

        # Mark user as online
        await self.set_user_presence(self.scope['user'].id, True)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chatroom_group_name,
            self.channel_name
        )

        # Mark user as offline
        await self.set_user_presence(self.scope['user'].id, False)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get('type', 'message')
        sender_id = self.scope['user'].id

        if event_type == 'message':
            message = data['message']
            parent_id = data.get('parent_id')
            # Save message to database
            msg = await self.save_message(sender_id, self.chatroom_id, message, parent_id)

            # Send message to room group
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender_id': sender_id,
                    'sender_name': self.scope['user'].get_full_name(),
                    'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'message_id': msg.id,
                    'parent_id': parent_id,
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
        elif event_type == 'reaction':
            message_id = data['message_id']
            emoji = data['emoji']
            action = data.get('action', 'add')  # 'add' or 'remove'
            if action == 'add':
                await self.add_reaction(sender_id, message_id, emoji)
            else:
                await self.remove_reaction(sender_id, message_id, emoji)
            reactions = await self.get_reactions(message_id)
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'reaction_update',
                    'message_id': message_id,
                    'reactions': reactions,
                }
            )
        elif event_type == 'edit_message':
            message_id = data['message_id']
            new_content = data['new_content']
            await self.edit_message(sender_id, message_id, new_content)
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'message_edited',
                    'message_id': message_id,
                    'new_content': new_content,
                }
            )
        elif event_type == 'delete_message':
            message_id = data['message_id']
            await self.delete_message(sender_id, message_id)
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'message_deleted',
                    'message_id': message_id,
                }
            )
        elif event_type == 'presence_update':
            # Broadcast presence update
            presence = await self.get_user_presence(sender_id)
            await self.channel_layer.group_send(
                self.chatroom_group_name,
                {
                    'type': 'presence_update',
                    'user_id': sender_id,
                    'is_online': presence['is_online'],
                    'last_seen': presence['last_seen'],
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': event['message'],
            'sender_id': event['sender_id'],
            'sender_name': event['sender_name'],
            'timestamp': event['timestamp'],
            'message_id': event['message_id'],
            'parent_id': event.get('parent_id'),
        }))

    async def typing(self, event):
        await self.send(text_data=json.dumps({
            'type': 'typing',
            'sender_id': event['sender_id'],
            'sender_name': event['sender_name'],
            'is_typing': event['is_typing'],
        }))

    async def read_receipt(self, event):
        await self.send(text_data=json.dumps({
            'type': 'read_receipt',
            'sender_id': event['sender_id'],
            'message_id': event['message_id'],
        }))

    async def reaction_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'reaction_update',
            'message_id': event['message_id'],
            'reactions': event['reactions'],
        }))

    async def message_edited(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message_edited',
            'message_id': event['message_id'],
            'new_content': event['new_content'],
        }))

    async def message_deleted(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message_deleted',
            'message_id': event['message_id'],
        }))

    async def presence_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'presence_update',
            'user_id': event['user_id'],
            'is_online': event['is_online'],
            'last_seen': event['last_seen'],
        }))

    @database_sync_to_async
    def save_message(self, sender_id, chatroom_id, message, parent_id=None):
        sender = User.objects.get(id=sender_id)
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        parent = None
        if parent_id:
            try:
                parent = Message.objects.get(id=parent_id)
            except Message.DoesNotExist:
                parent = None
        return Message.objects.create(chatroom=chatroom, sender=sender, content=message, parent=parent)

    @database_sync_to_async
    def mark_message_read(self, user_id, message_id):
        try:
            message = Message.objects.get(id=message_id)
            MessageReadStatus.objects.get_or_create(message=message, user_id=user_id)
        except Message.DoesNotExist:
            pass

    @database_sync_to_async
    def add_reaction(self, user_id, message_id, emoji):
        message = Message.objects.get(id=message_id)
        user = User.objects.get(id=user_id)
        Reaction.objects.get_or_create(message=message, user=user, emoji=emoji)

    @database_sync_to_async
    def remove_reaction(self, user_id, message_id, emoji):
        try:
            reaction = Reaction.objects.get(message_id=message_id, user_id=user_id, emoji=emoji)
            reaction.delete()
        except Reaction.DoesNotExist:
            pass

    @database_sync_to_async
    def get_reactions(self, message_id):
        reactions = Reaction.objects.filter(message_id=message_id).values('emoji').annotate(count=models.Count('id'))
        return list(reactions)

    @database_sync_to_async
    def edit_message(self, user_id, message_id, new_content):
        try:
            message = Message.objects.get(id=message_id, sender_id=user_id)
            message.content = new_content
            message.edited = True
            message.save()
        except Message.DoesNotExist:
            pass

    @database_sync_to_async
    def delete_message(self, user_id, message_id):
        try:
            message = Message.objects.get(id=message_id, sender_id=user_id)
            message.deleted = True
            message.save()
        except Message.DoesNotExist:
            pass

    @database_sync_to_async
    def set_user_presence(self, user_id, is_online):
        user = User.objects.get(id=user_id)
        presence, created = UserPresence.objects.get_or_create(user=user)
        presence.is_online = is_online
        if not is_online:
            from django.utils.timezone import now
            presence.last_seen = now()
        presence.save()

    @database_sync_to_async
    def get_user_presence(self, user_id):
        try:
            presence = UserPresence.objects.get(user_id=user_id)
            return {'is_online': presence.is_online, 'last_seen': presence.last_seen.strftime('%Y-%m-%d %H:%M:%S') if presence.last_seen else None}
        except UserPresence.DoesNotExist:
            return {'is_online': False, 'last_seen': None}
