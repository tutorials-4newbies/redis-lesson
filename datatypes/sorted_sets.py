import redis

r = redis.Redis(decode_responses=True)


res1 = r.zadd("racer_scores", {"Norem": 10})
print(res1)  # >>> 1

res2 = r.zadd("racer_scores", {"Castilla": 12})
print(res2)  # >>> 1

res3 = r.zadd(
    "racer_scores",
    {"Sam-Bodden": 8, "Royce": 10, "Ford": 6, "Prickett": 14, "Castilla": 12},
)
print(res3)  # >>> 4


res4 = r.zrange("racer_scores", 0, -1)
print(
    res4
)  # >>> ['Ford', 'Sam-Bodden', 'Norem', 'Royce', 'Castilla', 'Prickett']

res5 = r.zrevrange("racer_scores", 0, -1)
print(
    res5
)  # >>> ['Prickett', 'Castilla', 'Royce', 'Norem', 'Sam-Bodden', 'Ford']

res6 = r.zrange("racer_scores", 0, -1, withscores=True)
print(
    res6
)  # >>> [('Ford', 6.0), ('Sam-Bodden', 8.0), ('Norem', 10.0), ('Royce', 10.0), ('Castilla', 12.0), ('Prickett', 14.0)]

res7 = r.zrangebyscore("racer_scores", "-inf", 10)
print(res7)  # >>> ['Ford', 'Sam-Bodden', 'Norem', 'Royce']

res8 = r.zrem("racer_scores", "Castilla")
print(res8)  # >>> 1

res9 = r.zremrangebyscore("racer_scores", "-inf", 9)
print(res9)  # >>> 2

res10 = r.zrange("racer_scores", 0, -1)
print(res10)  # >>> ['Norem', 'Royce', 'Prickett']


res11 = r.zrank("racer_scores", "Norem")
print(res11)  # >>> 0

res12 = r.zrevrank("racer_scores", "Norem")
print(res12)  # >>> 2

res13 = r.zadd(
    "racer_scores",
    {
        "Norem": 0,
        "Sam-Bodden": 0,
        "Royce": 0,
        "Ford": 0,
        "Prickett": 0,
        "Castilla": 0,
    },
)
print(res13)  # >>> 3

res14 = r.zrange("racer_scores", 0, -1)
print(
    res14
)  # >>> ['Castilla', 'Ford', 'Norem', 'Prickett', 'Royce', 'Sam-Bodden']

res15 = r.zrangebylex("racer_scores", "[A", "[L")
print(res15)  # >>> ['Castilla', 'Ford']

res16 = r.zadd("racer_scores", {"Wood": 100})
print(res16)  # >>> 1

res17 = r.zadd("racer_scores", {"Henshaw": 100})
print(res17)  # >>> 1

res18 = r.zadd("racer_scores", {"Henshaw": 150})
print(res18)  # >>> 0

res19 = r.zincrby("racer_scores", 50, "Wood")
print(res19)  # >>> 150.0

res20 = r.zincrby("racer_scores", 50, "Henshaw")
print(res20)  # >>> 200.0
