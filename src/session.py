import asyncio
import json
from time import time
from uuid import uuid4
from connection import ClientConnection

timestamp = lambda : int(time())

class PlayerSession:
    
    def __init__(self, uid: str, nick: str,  conn: ClientConnection):
        self.session_id = uuid4()
        self.user_id = uid
        self.nickname = nick
        self.connection = conn
        self.client_addr = conn.client_addr
        self.start_time = timestamp()
        self.last_activity = timestamp()

    def __repr__(self) -> str:
        return f'PlayerSession({self.session_id}, {self.user_id}, {self.nickname}, {self.client_addr})'

    def to_json(self) -> str:
        return json.dumps({'session_id': str(self.session_id),
            'user_id': self.user_id,
            'nickname': self.nickname,
            'client_addr': self.client_addr,
            'last_activity': self.last_activity})

