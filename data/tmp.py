
import json
import pickle
from time import perf_counter as pc

path = 'subjects.json'

# 写法1
records = [json.loads(line) for line in open(path)]
print(len(records))
t1 = pc()
for rec in records:
    i = records.index(rec)
    if type(rec['year']) == list:
        records[i]['year'] = 1900

time1 = pc() - t1
print(time1)

# 写法2
records = [json.loads(line) for line in open(path)]
print(len(records))
t2 = pc()
for i, v  in enumerate(records):
    if type(v['year']) == list:
        records[i]['year'] = 1900
time2 = pc() - t2
print(time2)

print(time1 // time2)









# t1 = pc()
# with open('jsondump.json', 'w') as f:
#     json.dump(records, f)
# print(pc()-t1)
# # jsondump.json 大小 25.1M


# t2 = pc()
# with open('jsondump_indent.json', 'w') as f:
#     json.dump(records, f, indent=4)
# print(pc()-t2)
# # jsondump_indent.json 大小 35M

# t3 = pc()
# with open('pickledump.json', 'wb') as f:
#     pickle.dump(records, f)
# print(pc()-t3)
# # jsondump_indent.json 大小 30.7M
