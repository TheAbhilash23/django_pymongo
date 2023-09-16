# remember to add the connection string in the config. This is just for illustrative purposes Only
from pymongo import MongoClient
from pymongo.database import Database

CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.0"

CLIENT = MongoClient(CONNECTION_STRING)

DATABASES = {}

for database in CLIENT.list_database_names():
    DATABASES[str(database)] = CLIENT[database]

# SETACTIVE_DATABASES = DATABASES['configurable_kyc'] if DATABASES['configurable_kyc'] is True else None


class DefaultDatabase(Database):
    def __init__(self, client: MongoClient, name: str, *args, **kwargs):
        super().__init__(client, name, *args, **kwargs)


DEFAULT_DB = DefaultDatabase(CLIENT, 'configurable_kyc')
