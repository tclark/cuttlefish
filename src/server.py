import asyncio
import sys

class Server:

    def __init__(self, config=None):
        if config:
            pass

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
        data = await reader.read(1024)
        message = data.decode()
        remote_addr = writer.get_extra_info('peername')
        print(f'Received "{message!r}" from {remote_addr!r}')
        response = b'ok'
        writer.write(response)
        await writer.drain()
        writer.close()
