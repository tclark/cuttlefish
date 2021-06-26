import asyncio
import json
from uuid import uuid4

from connection import ClientConnection
from session import PlayerSession

class Login:

    def __init__(self):
        self._client_connection = None
    
    async def login(self, conn: ClientConnection) -> PlayerSession:
        message = await conn.read()
        action = message.body.get('action')
        params = message.body.get('params', {})
        if action != 'login':
            pass # handle error here
        uid = params.get('user_id')
        if not uid:
            pass  # handle error here
        nick = params.get('nick', '')
        session = PlayerSession(uid, nick, conn)
        await conn.send(session.to_json())
        return session





