# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope["user"]
        print("Connected user:", user, "Authenticated:", user.is_authenticated)
        if user.is_anonymous:
            self.close()
            return
        print("WebSocket connected for user:", user)
        self.roome_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.group_name = f"chat_{self.roome_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat.message",
                "message": message,
            },
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))

    