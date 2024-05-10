a = input()
b = input()

a = a.split() 
a = [int(i) for i in a]
a.sort()

b = b.split() 
b = [int(i) for i in b]
b.sort() 

print(a == b)
if not a == b:
    for i, j in zip(a, b):
        if not i==j:
            print(i, '   ', j)