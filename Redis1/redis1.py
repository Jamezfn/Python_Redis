import redis
from time import sleep

client = redis.Redis(host='127.0.0.1', port=6379)

### demo the strings

client.set('language', 'Python')
print(client.get('language'))

client.set('language', 'Python', px = 10000)
print(client.get('language'))
print(client.ttl('language'))
sleep(7)
print(client.ttl('language'))

client.set('language', 'Python')
print(client.expire('language', 10))
print(client.ttl('language'))
sleep(7)
print(client.ttl('language'))
