# middleware.py
import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from jwt import InvalidTokenError

User = get_user_model()

@database_sync_to_async
def get_user_from_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload["user_id"]
        print('this is user id from token:', user_id)
        return User.objects.get(id=user_id)
    except (InvalidTokenError, User.DoesNotExist, KeyError):
        return AnonymousUser()

class JWTAuthMiddleware:
    """
    Custom middleware that reads JWT from:
      1. query_string (ws://...?token=abc)     ← easiest for testing
      2. cookie (access_token)                 ← production-ready
      3. subprotocols (optional, later)
    """
    def __init__(self, app):
        self.app = app
        print('JWTAuthMiddleware initialized.')
    async def __call__(self, scope, receive, send):
        # Default to Anonymous
        scope["user"] = AnonymousUser()

        # 1. Try query string first (great for dev)
        query_string = scope.get("query_string", b"").decode()
        token = parse_qs(query_string).get("token", [None])[0]
        
        # 2. Try cookie second (better for production)
        if not token:
            cookies = scope.get("cookies", {})
            token = cookies.get("access_token")
        if token:
            user = await get_user_from_jwt(token)
            scope["user"] = user

        return await self.app(scope, receive, send)