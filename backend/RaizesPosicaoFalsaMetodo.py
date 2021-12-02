from math import sin, cos, tan, asin, acos, atan, pow, e, fabs, sqrt, log, ceil

a = float(input('Type it "a" from [a,b]: '))
b = float(input('Type it "b" from [a,b]: '))
precision = float(input('Type it precision: '))

def f(number):
    return number*log(number,10) - 1

y = float('infinity')
contador = 0

while (contador <= 500) or (fabs(y) > precision) or (y == 0):
    x = (a*fabs(f(b)) + b*fabs(f(a))) / (fabs(f(b)) + fabs(f(a)))
    y = f(x)

    if (f(a) > 0) and (y > 0) or (f(a) < 0) and (y < 0):
        a = x
    elif (f(b) > 0) and (y>0) or (f(b) < 0) and (y < 0):
        b = x

    contador+=1

print(f'The root value is {x}')





      








    



