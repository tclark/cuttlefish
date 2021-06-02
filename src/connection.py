import asyncio
from asyncio import StreamReader, StreamWriter
from collections import namedtuple
import json
from typing import Any, Optional

Message = namedtuple("Message", "headers body")

class Headers:

    def __init__(self, 
        content_type: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_length: int = 0,
        **kwargs):
        self.content_type = content_type
        self.content_length = content_length
        self.content_encoding = content_encoding
        for k,v in kwargs.items():
            super().__setattr__(k, v)


class ClientConnection:

    def __init__(self, rdr: StreamReader, wtr: StreamWriter):
        self._reader = rdr
        self._writer = wtr

    async def read(self) -> Message:
        headers = await self._read_headers()
        body = await self._read_body(headers)
        return Message(headers, body)

    async def _read_headers(self) -> Headers:
        data = await self._reader.readuntil(separator=b'\n\n')
        data_d = json.loads(data.decode())
        data_d_snek = {key.lower().replace('-', '_') : val 
            for key, val in data_d.items()}
        return Headers(**data_d_snek)

    async def _read_body(self, headers: Headers) -> dict[str, Any]:
        data = await self._reader.readexactly(headers.content_length)
        body = {}
        if (headers.content_encoding == 'utf-8' and
           headers.content_type == 'application/json'):
            body = json.loads(data.decode())
        # always include the bytes
        body['raw'] = data
        return body
