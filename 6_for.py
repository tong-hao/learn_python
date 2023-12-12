print("#### list:")
l = [1,2,3]
for item in l:
    print (item)

print("#### map:")
map = {"a":1, "b":2}
for item in map:
    print(item)
for k in map.keys():
    print(k)
for v in map.values():
    print(v)
for k,v in map.items():
    print(k,v)

print("#### range:")
for i in range(0, 10, 2):
    print(i)
