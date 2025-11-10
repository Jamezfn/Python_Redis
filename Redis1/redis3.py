import redis

### demo the hashes

client = redis.Redis(host='127.0.0.1', port=6379)

client.hset('Hero', 'Name', 'Drow Ranger')
client.hset('Hero', 'Health', '600')
client.hset('Hero', 'Mana', '200')

print(client.hgetall('Hero'))
