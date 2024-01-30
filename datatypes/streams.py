import redis

r = redis.Redis(decode_responses=True)

res1 = r.xadd(
    "race:france",
    {"rider": "Castilla", "speed": 30.2, "position": 1, "location_id": 1},
)
print(res1)  # >>> 1692629576966-0

res2 = r.xadd(
    "race:france",
    {"rider": "Norem", "speed": 28.8, "position": 3, "location_id": 1},
)
print(res2)  # >>> 1692629594113-0

res3 = r.xadd(
    "race:france",
    {"rider": "Prickett", "speed": 29.7, "position": 2, "location_id": 1},
)
print(res3)  # >>> 1692629613374-0


res4 = r.xrange("race:france", "1691765278160-0", "+", 2)
print(
    res4
)  # >>> [('1692629576966-0', {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}), ('1692629594113-0', {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'})]

res5 = r.xread(streams={"race:france": 0}, count=100, block=300)
print(
    res5
)  # >>> [['race:france', [('1692629576966-0', {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}), ('1692629594113-0', {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}), ('1692629613374-0', {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'})]]]

res6 = r.xadd(
    "race:france",
    {"rider": "Castilla", "speed": 29.9, "position": 1, "location_id": 2},
)
print(res6)  # >>> 1692629676124-0

res7 = r.xlen("race:france")
print(res7)  # >>> 4


res8 = r.xadd("race:usa", {"racer": "Castilla"}, id="0-1")
print(res8)  # >>> 0-1

res9 = r.xadd("race:usa", {"racer": "Norem"}, id="0-2")
print(res9)  # >>> 0-2

try:
    res10 = r.xadd("race:usa", {"racer": "Prickett"}, id="0-1")
    print(res10)  # >>> 0-1
except redis.exceptions.ResponseError as e:
    print(e)  # >>> WRONGID

# Not yet implemented

res11 = r.xrange("race:france", "-", "+")
print(
    res11
)  # >>> [('1692629576966-0', {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}), ('1692629594113-0', {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}), ('1692629613374-0', {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}), ('1692629676124-0', {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'})]

res12 = r.xrange("race:france", 1692629576965, 1692629576967)
print(
    res12
)  # >>> [('1692629576966-0', {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'})]

res13 = r.xrange("race:france", "-", "+", 2)
print(
    res13
)  # >>> [('1692629576966-0', {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}), ('1692629594113-0', {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'})]

res14 = r.xrange("race:france", "(1692629594113-0", "+", 2)
print(
    res14
)  # >>> [('1692629613374-0', {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}), ('1692629676124-0', {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'})]

res15 = r.xrange("race:france", "(1692629676124-0", "+", 2)
print(res15)  # >>> []

res16 = r.xrevrange("race:france", "+", "-", 1)
print(
    res16
)  # >>> [('1692629676124-0', {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'})]

res17 = r.xread(streams={"race:france": 0}, count=2)
print(
    res17
)  # >>> [['race:france', [('1692629576966-0', {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}), ('1692629594113-0', {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'})]]]

res18 = r.xgroup_create("race:france", "france_riders", "$")
print(res18)  # >>> True

res19 = r.xgroup_create("race:italy", "italy_riders", "$", mkstream=True)
print(res19)  # >>> True

r.xadd("race:italy", {"rider": "Castilla"})
r.xadd("race:italy", {"rider": "Royce"})
r.xadd("race:italy", {"rider": "Sam-Bodden"})
r.xadd("race:italy", {"rider": "Prickett"})
r.xadd("race:italy", {"rider": "Norem"})

res20 = r.xreadgroup(
    streams={"race:italy": ">"},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(
    res20
)  # >>> [['race:italy', [('1692629925771-0', {'rider': 'Castilla'})]]]

res21 = r.xreadgroup(
    streams={"race:italy": 0},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(
    res21
)  # >>> [['race:italy', [('1692629925771-0', {'rider': 'Castilla'})]]]

res22 = r.xack("race:italy", "italy_riders", "1692629925771-0")
print(res22)  # >>> 1

res23 = r.xreadgroup(
    streams={"race:italy": 0},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res23)  # >>> [['race:italy', []]]

res24 = r.xreadgroup(
    streams={"race:italy": ">"},
    consumername="Bob",
    groupname="italy_riders",
    count=2,
)
print(
    res24
)  # >>> [['race:italy', [('1692629925789-0', {'rider': 'Royce'}), ('1692629925790-0', {'rider': 'Sam-Bodden'})]]]

res25 = r.xpending("race:italy", "italy_riders")
print(
    res25
)  # >>> {'pending': 2, 'min': '1692629925789-0', 'max': '1692629925790-0', 'consumers': [{'name': 'Bob', 'pending': 2}]}

res26 = r.xpending_range("race:italy", "italy_riders", "-", "+", 10)
print(
    res26
)  # >>> [{'message_id': '1692629925789-0', 'consumer': 'Bob', 'time_since_delivered': 31084, 'times_delivered': 1}, {'message_id': '1692629925790-0', 'consumer': 'Bob', 'time_since_delivered': 31084, 'times_delivered': 1}]

res27 = r.xrange("race:italy", "1692629925789-0", "1692629925789-0")
print(res27)  # >>> [('1692629925789-0', {'rider': 'Royce'})]

res28 = r.xclaim(
    "race:italy", "italy_riders", "Alice", 60000, ["1692629925789-0"]
)
print(res28)  # >>> [('1692629925789-0', {'rider': 'Royce'})]

res29 = r.xautoclaim("race:italy", "italy_riders", "Alice", 1, "0-0", 1)
print(
    res29
)  # >>> ['1692629925790-0', [('1692629925789-0', {'rider': 'Royce'})]]

res30 = r.xautoclaim(
    "race:italy", "italy_riders", "Alice", 1, "(1692629925789-0", 1
)
print(res30)  # >>> ['0-0', [('1692629925790-0', {'rider': 'Sam-Bodden'})]]

res31 = r.xinfo_stream("race:italy")
print(
    res31
)  # >>> {'length': 5, 'radix-tree-keys': 1, 'radix-tree-nodes': 2, 'last-generated-id': '1692629926436-0', 'groups': 1, 'first-entry': ('1692629925771-0', {'rider': 'Castilla'}), 'last-entry': ('1692629926436-0', {'rider': 'Norem'})}

res32 = r.xinfo_groups("race:italy")
print(
    res32
)  # >>> [{'name': 'italy_riders', 'consumers': 2, 'pending': 2, 'last-delivered-id': '1692629925790-0'}]

res33 = r.xinfo_consumers("race:italy", "italy_riders")
print(
    res33
)  # >>> [{'name': 'Alice', 'pending': 2, 'idle': 199332}, {'name': 'Bob', 'pending': 0, 'idle': 489170}]

r.xadd("race:italy", {"rider": "Jones"}, maxlen=2)
r.xadd("race:italy", {"rider": "Wood"}, maxlen=2)
r.xadd("race:italy", {"rider": "Henshaw"}, maxlen=2)

res34 = r.xlen("race:italy")
print(res34)  # >>> 8

res35 = r.xrange("race:italy", "-", "+")
print(
    res35
)  # >>> [('1692629925771-0', {'rider': 'Castilla'}), ('1692629925789-0', {'rider': 'Royce'}), ('1692629925790-0', {'rider': 'Sam-Bodden'}), ('1692629925791-0', {'rider': 'Prickett'}), ('1692629926436-0', {'rider': 'Norem'}), ('1692630612602-0', {'rider': 'Jones'}), ('1692630641947-0', {'rider': 'Wood'}), ('1692630648281-0', {'rider': 'Henshaw'})]

r.xadd("race:italy", {"rider": "Smith"}, maxlen=2, approximate=False)

res36 = r.xrange("race:italy", "-", "+")
print(
    res36
)  # >>> [('1692630648281-0', {'rider': 'Henshaw'}), ('1692631018238-0', {'rider': 'Smith'})]

res37 = r.xtrim("race:italy", maxlen=10, approximate=False)
print(res37)  # >>> 0

res38 = r.xtrim("race:italy", maxlen=10)
print(res38)  # >>> 0

res39 = r.xrange("race:italy", "-", "+")
print(
    res39
)  # >>> [('1692630648281-0', {'rider': 'Henshaw'}), ('1692631018238-0', {'rider': 'Smith'})]

res40 = r.xdel("race:italy", "1692631018238-0")
print(res40)  # >>> 1

res41 = r.xrange("race:italy", "-", "+")
print(res41)  # >>> [('1692630648281-0', {'rider': 'Henshaw'})]
