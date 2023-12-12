dir = "/Users/ht/code/python_learnning/"

print("#### write:")
f = open(dir + "1.txt", "w", encoding="utf-8")
f.write("1\n")
f.write("2\n")
f.write("3\n")
f.write("四\n")
f.close()

print("#### read:")
f = open(dir + "1.txt", "r", encoding="utf-8")

print("# read by lines:")
lines = f.readlines()
for line in lines:
    print(line)

print("\n# read by byte:")
str_10bytes = f.read(2)
print(str_10bytes)

print("\n# read full file:")
print(f.read())

# close
f.close()


print("#### with open:")
with open(dir + "1.txt", "r", encoding="utf-8") as f:
    print(f.readline()) # 第一行
    print(f.readline()) # 第二行


