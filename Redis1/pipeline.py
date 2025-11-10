import redis

client = redis.Redis(host='127.0.0.1', port=6379)

pipline = client.pipeline(transaction=False)
pipline.sadd('mylist', '1stElement')
pipline.sadd('mylist', '1stElement')
pipline.sadd('mylist', '3rdElement')
pipline.sadd('mylist', '4thElement')
pipline.sadd('mylist', '5thElement')
print(pipline.smembers('mylist'))
print(pipline.execute())

with client.pipeline() as mypipe:
    print(mypipe.scard('mylist'))
