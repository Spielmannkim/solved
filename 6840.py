N = 3
x = []
for i in range(N):
    x.append(int(input()))
a = max(x)
b = min(x)
x.remove(a)
x.remove(b)
print(x[0])