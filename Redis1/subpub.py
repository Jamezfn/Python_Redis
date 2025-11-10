import redis

env = 'dev'

client = redis.Redis(host='127.0.0.1', port=6379)

p = client.pubsub()
p.subscribe(env)

while True:
    message = p.get_message()
    if message:
        print(dir(message['data']))
