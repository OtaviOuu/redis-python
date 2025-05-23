from redis import Redis
from .connections_options import connection_options

class RedisConnectionHandle:
    def __init__(self):
        self.__host = connection_options["HOST"]
        self.__port = connection_options["PORT"]
        self.__db = connection_options["DB"]
        self.__connection = None
    
    def connect(self) -> Redis:
        self.__connection = Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db
        )

        return self.__connection
    
    def get_connection(self) -> Redis:
        return self.__connection