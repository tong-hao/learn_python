l = []
l.append("item1")
l.append("item2")
l.append("item3")

l.remove("item2")

l[0] = "001"
l.append(2)

print(l)
print("len:" + str(len(l)))

l2 = [1,2,3]
print("max:" + str(max(l2)))
print("min:" + str(min(l2)))
