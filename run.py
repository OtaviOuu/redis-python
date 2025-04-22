from models.connection.redis.connection import RedisConnectionHandle

from repositories.redis.repo import RedisRepository

redis_connection = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_connection)

redis_repository.insert("key1", "value1")



