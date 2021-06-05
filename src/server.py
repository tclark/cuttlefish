import asyncio
from asyncio import StreamReader, StreamWriter
import sys

import connection
import login


class DefaultConfig:
    login_handler = login.Login()


class Config(DefaultConfig):
    def __init__(self, ** kwargs):
        super().__init__()
        for k,v in kwargs.items():
            super().__setattr__(k,v)

class Server:

    def __init__(self, config: Config = None):
        self.config = config or DefaultConfig()

    def bind_to(self, addr: str , port: int):
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

    async def _handle(self, reader: StreamReader, writer: StreamWriter) -> None:
        conn = connection.ClientConnection(reader, writer)
        player_session = await self.config.login_handler.login(conn)
        print(player_session)
        return None
