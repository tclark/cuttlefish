import asyncio
from connection import ClientConnection

class PlayerSession:
    pass


class Login:

    def __init__(self):
        self._client_connection = None
    
    async def login(self, conn: ClientConnection) -> PlayerSession:
        self._client_connection = conn
        message = await conn.read()
        print(f'received: {message}')


