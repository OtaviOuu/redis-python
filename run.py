from models.connection.redis.connection import RedisConnectionHandle

redis_connection = RedisConnectionHandle().connect()
print(redis_connection)