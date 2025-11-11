import redis
import json

env = 'dev'
client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)  # Important!
p = client.pubsub()
p.subscribe(env)

print(f"Subscribed to channel: {env}")

while True:
    message = p.get_message(ignore_subscribe_messages=True, timeout=1.0)
    
    if message:
        data = message['data']
        print("Received:", data)
        
        # Now safe to inspect attributes if it's an object
        if isinstance(data, (dict, list, str)):
            print("Type:", type(data))
            print("Dir:", dir(data)[:10])  # First 10 attributes
        else:
            print("Raw data type:", type(data))
            print("String value:", str(data))
