from django.urls import re_path

from . import consumers
print('hey route 1')
websocket_urlpatterns = [
    # match ws://<host>/ws/chat/<room>?token=<jwt>
    re_path(r"ws/chat/(?P<room_name>[^/]+)/?$", consumers.ChatConsumer.as_asgi()),
]
# write the path which match the following patter of request


#  'ws://'
#             + window.location.host
#             + '/ws/chat/'
#             + roomName
#             + '?token=' + token