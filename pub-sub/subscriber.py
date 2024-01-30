import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True
)

receiver = r.pubsub()

receiver.subscribe('channel-1')

for message in receiver.listen():
    print(message)
