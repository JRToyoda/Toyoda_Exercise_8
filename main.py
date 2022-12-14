data = [5, 3, 7]

a = data[2]  # 7
b = data[-1]  # 7
c = len(data)  # 3
d = data[0:2]  # [5, 3]
e = 0 in data  # False
f = data + [2, 10, 5]  # [5, 3, 7, 2, 10, 5]
g = tuple(data)  # (5, 3, 7)

data[0] = -data[0]
data.append(10)
data.insert(2, 22)
del data[1]
data.sort()

# [-5, 7, 10, 22]

print()  # input any variable from above
