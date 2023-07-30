import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from chat.models import Message, Chat, Account


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_id = str(self.scope["url_route"]["kwargs"]["chat_id"])
        self.chat = await database_sync_to_async(Chat.objects.get)(id=self.chat_id)

        await self.channel_layer.group_add(self.chat_id, self.channel_name)

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)

        type = text_data.get("type", None)
        message = text_data.get("message", None)
        sender = text_data.get("sender", None)

        if type == "text_message":
            sender = await database_sync_to_async(Account.objects.get)(id=sender)
            message = await database_sync_to_async(Message.objects.create)(
                sender=sender,
                text=message,
                chat=self.chat
            )

        await self.channel_layer.group_send(self.chat_id, {
            "type": "text_message",
            "message": message.text,
            "sender": sender.name
        })

    async def text_message(self, event):
        message = event["message"]
        sender = event.get("sender")

        returned_data = {
            "type": "text_message",
            "sender": sender,
            "message": message,
            "chat_id": self.chat_id
        }
        await self.send(json.dumps(
            returned_data
        ))
