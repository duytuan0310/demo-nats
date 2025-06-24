import os
import asyncio
from nats.aio.client import Client

class NatsServer:
    def __init__(self, server_url: str):
        self.server_url = server_url or os.getenv("NATS_SERVER_URL", "nats://localhost:4222")
async def connect(self):