from redis import Redis


class RedisRepository:
    # service → repository → db (e usa model como estrutura)

    def __init__(self, redis_connection: Redis) -> None:
        # injeção de dependência do redis_connection
        self.__redis_connection = redis_connection

    def insert(self, key: str, value: any) -> None:
        self.__redis_connection.set(key, value)
        
    def get(self, key: str) -> any:
        value = self.__redis_connection.get(key).decode("utf-8")
        return value