from aiochclient import ChClient
from aiohttp import ClientSession

from models.models import MessageDto
from core.config import settings


class ClickhouseWriter:
    async def __aenter__(self):
        self.session = ClientSession()
        self.client = ChClient(self.session, settings.clickhouse_brokers[0])
        return self

    async def write(self, rows: list[MessageDto]):
        raw_query = 'INSERT INTO data_analytics.event_table ({}) VALUES'
        query = raw_query.format(', '.join(MessageDto.__annotations__.keys()))
        await self.client.execute(query, *rows)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
