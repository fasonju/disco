import random

lam = lambda x: random.randint(x,365)
input1 = int(input('input'))
print(input1)
for i in range(input1):
    x = random.randint(0,365)
    print(f"a {x} {lam(x)}" )
    