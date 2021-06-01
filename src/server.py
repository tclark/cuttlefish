import asyncio
import sys

import connection
import login

class Server:

    def __init__(self, config=None):
        if config:
            pass
        self._login_handler = login.Login()    

    def bind_to(self, addr, port):
        self.addr = addr
        self.port = port

    async def _start(self):
        self._server = await asyncio.start_server(
            self._handle, self.addr, self.port)

        async with self._server:
            await self._server.serve_forever()

    def run(self):
        try:
            asyncio.run(self._start())
        except KeyboardInterrupt:
            sys.exit()

    async def _handle(self, reader, writer):
        conn = connection.ClientConnection(reader, writer)
        player_session = await self._login_handler.login(conn)
        return None
