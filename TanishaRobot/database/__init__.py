

from async_pymongo import AsyncClient

from TanishaRobot import MONGO_DB_URI

DBNAME = "TanishaRobot"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
