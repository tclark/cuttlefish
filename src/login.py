import asyncio
import json
from uuid import uuid4

from connection import ClientConnection

class PlayerSession:
    
    def __init__(self, uid: str, nick: str,  conn: ClientConnection):
        self.session_id = uuid4()
        self.user_id = uid
        self.nickname = nick
        self.connection = conn
        self.client_addr = conn.client_addr

    def __repr__(self):
        return f'PlayerSession({self.session_id}, {self.user_id}, {self.nickname}, {self.client_addr})'

    def to_json(self):
        return json.dumps({'session_id': str(self.session_id),
            'user_id': self.user_id,
            'nickname': self.nickname,
            'client_addr': self.client_addr})

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
        return PlayerSession(uid, nick, conn)




