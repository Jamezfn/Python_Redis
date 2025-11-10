import redis

client = redis.Redis(host='127.0.0.1', port=6379)

### demo the sets

client.sadd('pylist', "value1", "value2", "value3", "value4")
client.sadd('plist', "value4", "value5", "value6", "value7")

print(client.sinter('pylist', 'plist'))
print(client.sunion('pylist', 'plist'))
print(client.scard('pylist'))
print(client.scard('plist'))
