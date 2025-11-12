## ⚡ Django Channels Overview

**Django Channels** extends Django’s capabilities beyond traditional HTTP, enabling support for protocols like **WebSocket** for real-time communication.

---

### 🔌 Protocol Routing with ASGI

To handle WebSocket connections, Django Channels uses the **Asynchronous Server Gateway Interface (ASGI)**. ASGI inspects incoming requests and routes them based on protocol:

```
HTTP → ASGI → urls.py → views.py  
WebSocket → ASGI → routing.py → consumers.py
```

WebSocket clients typically connect using a scoped endpoint such as `/ws/chat`.

---

### 🧠 Consumers: Handling WebSocket Logic

Django Channels defines two types of consumers to process WebSocket events:

#### 1. **Synchronous Consumer** (`WebSocketConsumer`)
- Processes one connection at a time.
- Uses `sync_to_async` to simulate asynchronous behavior.
- Suitable for simple or low-traffic applications.


```python
# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
```

#### 2. **Asynchronous Consumer** (`AsyncWebSocketConsumer`)
- Designed for production use.
- Handles thousands of concurrent connections efficiently.
- Fully compatible with Django Channels’ async architecture.

```python
# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
````
---

### 🔁 Channel Layer: Instance Communication

The **channel layer** enables communication between different consumer instances using a backing store like **Redis**.

#### Components:
- **Channel**: A unique mailbox for each consumer instance.
- **Group**: A collection of channels used to broadcast messages to multiple clients simultaneously.

---

### 🚀 Daphne: ASGI-Compatible Server

**Daphne** is the recommended server for running Django Channels in production. It supports both HTTP and WebSocket protocols.

```bash
daphne -p 8000 MyProject.asgi:application
```

---

### 🐳 Redis via Docker (Recommended)

To enable the channel layer, Redis is commonly used as the backing store. You can quickly spin up Redis using Docker:

```bash
docker run -d -p 6379:6379 redis
```

---

