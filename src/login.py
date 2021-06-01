import asyncio


class Login:

    def __init__(self):
        self._client_connection = None
    
    async def login(self, conn):
        self._client_connection = conn
        message = await conn.read()
        print(f'received: {message}')


