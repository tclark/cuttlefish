import asyncio
from collections import namedtuple
import json

Message = namedtuple("Message", "headers body")

class Headers:

    def __init__(self, 
        content_type=None,
        content_encoding=None,
        content_length=None,
        **kwargs):
        self.content_type = content_type
        self.content_length = content_length
        self.content_encoding = content_encoding
        for k,v in kwargs.items():
            super().__setattr__(k, v)


class ClientConnection:

    def __init__(self, rdr, wtr):
        self._reader = rdr
        self._writer = wtr

    async def read(self):
        headers = await self._read_headers()
        body = await self._read_body(headers)
        return Message(headers, body)

    async def _read_headers(self):
        data = await self._reader.readuntil(separator=b'\n\n')
        data_d = json.loads(data.decode())
        data_d_snek = {key.lower().replace('-', '_') : val 
            for key, val in data_d.items()}
        return Headers(**data_d_snek)

    async def _read_body(self, headers):
        data = await self._reader.readexactly(headers.content_length)
        if (headers.content_encoding == 'utf-8' and
           headers.content_type == 'application/json'):
            return json.loads(data.decode())
        # else just send on the bytes
        return data
