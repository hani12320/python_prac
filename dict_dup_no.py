list = [1,2,2,3,3,3]
d = {}
for i in list:
    d[i] = d.get(i, 0) + 1
print(d)
