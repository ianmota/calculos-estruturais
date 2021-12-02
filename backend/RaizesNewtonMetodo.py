import math

x0 = float(input('Type it X0 (start kick): '))
precision = float(input('Type it precision: '))

def derivadaf(number):
    return 2*number + 1

def f(number):
    return math.pow(number,2) + number - 6

results = [x0]
y = precision
while (math.fabs(y) >= precision) or (y != 0):
    x = x0 - (f(x0)/derivadaf(x0))
    results.append(x)
    x0 = x
    y = f(x)
 
print(f'The root value is {x}')
for i in results:
    print(f'The possible results are {i}')







