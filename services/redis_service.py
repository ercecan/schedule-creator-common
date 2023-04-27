import os
import redis
from dotenv import load_dotenv, find_dotenv
import json


class RedisService:
    load_dotenv(find_dotenv())

    def __init__(self):
        self.host = os.getenv('REDIS_HOST')
        self.port = 6379
        self.redis = redis.from_url(f'redis://{self.host}')

    def set_val(self, key, val):
        stringified_val = json.dumps(val)
        self.redis.set(key, stringified_val)

    def delete_key(self, key):
        self.redis.delete(key)

    def get_val(self, key):
        response = self.redis.get(key)
        json_response = json.loads(response)
        return json_response
