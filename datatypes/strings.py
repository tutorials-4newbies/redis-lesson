import redis

r = redis.Redis(decode_responses=True)

res1 = r.set("bike:1", "Deimos", ex=10)
print(res1)  # True
res2 = r.get("bike:1")
print(res2)  # Deimos


res3 = r.set("bike:1", "bike", nx=True)
print(res3)  # None
print(r.get("bike:1"))  # Deimos
res4 = r.set("bike:1", "bike", xx=True)
print(res4)  # True


res5 = r.mset({"bike:1": "Deimos", "bike:2": "Ares", "bike:3": "Vanth"})
print(res5)  # True
res6 = r.mget(["bike:1", "bike:2", "bike:3"])
print(res6)  # ['Deimos', 'Ares', 'Vanth']


r.set("total_crashes", 0)
res7 = r.incr("total_crashes")
print(res7)  # 1
res8 = r.incrby("total_crashes", 10)
print(res8)  # 11