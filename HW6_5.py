l = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]
line = str(l)
l.clear()

for x in line:
    try:
        x = int(x)
        l.append(x)
    except:
        pass

print(l)