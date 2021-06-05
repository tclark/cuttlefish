import asyncio
from connection import ClientConnection

class PlayerSession:
    
    def __init__(self, uid: str, nick: str,  conn: ClientConnection):
        self.user_id = uid
        self.nickname = nick
        self.connection = conn
        self.client_addr = conn.client_addr

    def __repr__(self):
        return f'PlayerSession({self.user_id}, {self.nickname}, {self.client_addr})'

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




