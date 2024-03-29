import redis

r = redis.Redis(decode_responses=True)
res1 = r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)
print(res1)
# >>> 4

res2 = r.hget("bike:1", "model")
print(res2)
# >>> 'Deimos'

res3 = r.hget("bike:1", "price")
print(res3)
# >>> '4972'

res4 = r.hgetall("bike:1")
print(res4)
# >>> {'model': 'Deimos', 'brand': 'Ergonom', 'type': 'Enduro bikes', 'price': '4972'}



res5 = r.hmget("bike:1", ["model", "price"])
print(res5)
# >>> ['Deimos', '4972']


res6 = r.hincrby("bike:1", "price", 100)
print(res6)
# >>> 5072
res7 = r.hincrby("bike:1", "price", -100)
print(res7)
# >>> 4972



res11 = r.hincrby("bike:1:stats", "rides", 1)
print(res11)
# >>> 1
res12 = r.hincrby("bike:1:stats", "rides", 1)
print(res12)
# >>> 2
res13 = r.hincrby("bike:1:stats", "rides", 1)
print(res13)
# >>> 3
res14 = r.hincrby("bike:1:stats", "crashes", 1)
print(res14)
# >>> 1
res15 = r.hincrby("bike:1:stats", "owners", 1)
print(res15)
# >>> 1
res16 = r.hget("bike:1:stats", "rides")
print(res16)
# >>> 3
res17 = r.hmget("bike:1:stats", ["crashes", "owners"])
print(res17)
# >>> ['1', '1']

