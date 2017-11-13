name = input("Enter your name:")
a = 0
D = []
while a < len(name):
    D.append(ord(name[a]))
    a += 1
b = str(sum(D))
x, c = 0, 0
while x < len(b):
    c += int(b[x])
    x += 1
tot = 0
while c > 0:
    dig = c % 10
    tot += dig
    c //= 10
print(tot)
