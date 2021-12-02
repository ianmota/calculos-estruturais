
from math import sin, cos, tan, pow, pi, e, exp, sqrt, acos, asin, atan

b = int(input('Digite o valor de (b) \n'))
a = int(input('Digite o valor de (a) \n'))
n = int(input('Digite o valor de (n) \n'))

h = float((b-a)/n)
result = []


while (a<=b):
    y = pow(e,pow(a,2))   
    result.append(y)
    a+=h


integrate1 = 0.0
for i in range(1,n):
    if (i%2) == 0:
        a = (h/3)*(2*result[i])
    else:
        a = (h/3)*(4*result[i])
    integrate1+=a

integrate2 = 0.0
integrate2 = integrate1 + (h/3)*(result [0] + result[n])
print(f'O resultado da integral é {integrate2}')