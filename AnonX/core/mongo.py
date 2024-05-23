from aiosqlite import connect as _mongo_client_
from aiosqlite import Database

import config

from ..logging import LOGGER

async def connect_to_mongodb():
    _mongo_async_ = await _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = await _mongo_client_(config.MONGO_DB_URI)
    mongodb = Database(_mongo_async_, 'Vip')
    pymongodb = Database(_mongo_sync_, 'Vip')
    return mongodb, pymongodb
