import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True
)

while True:
    message = input("Enter the message you want to send to channel-1: ")

    r.publish("channel-1", message)
