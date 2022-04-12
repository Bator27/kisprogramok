import math
import random
a = random.randint(2,10)
b = random.randint(2,10)
c = random.randint(2,10)


def kerület (a,b,c):
    return a+b+c

def terület ():
    s = kerület/2
    return s*(math.sqrt((s-a)*(s-b)*(s-c)))

print(a,b,c)
print(f'a háromszög kerülete {a+b+c}')
print('Héron képlet')
s = k/2
