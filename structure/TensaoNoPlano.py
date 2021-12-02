#Bibliotecas importadas
import math as m

""""
#Váriáveis
tx = float(input('Tensão em x: '))
ty = float(input('Tensão em y: '))
tc = float(input('Tensão de cisalhamento: '))
ang = float(input('Ângulo (em radianos): '))
"""
#Váriáveis
tx = float(0.317)
ty = float(0.6338)
tc = float(0)
ang = float(21)

results = []

#Conversões
a = m.radians(ang)

#Equações
tx1 = (tx+ty)/2 + (tx-ty)*m.cos(2*a)/2 + tc*m.sin(2*a)
tc1 = (tx-ty)*m.sin(2*a)/2 - tc*m.cos(2*a)
tx2 = tx + ty - tx1

results.append(tx1)
results.append(tc1)
results.append(tx2)

print(f'A tensão normal é {results[0]}')
print(f'A tensão de cisalhamento é {results[1]}') 
print(f'A tensão normal em y é ')    

