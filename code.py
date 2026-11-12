def check(mass):
    for i in range(len(mass)):
        if mass[i] > mass[i + 1]:
            return False
    return True

a = ['p', 'r', 't']
b = ['a', 'b', 'z']

if check(a):
    print(1)
if check(b):
    print(2)
print(-1)
