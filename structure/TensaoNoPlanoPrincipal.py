import math as m

#Variáveis
tx = float(8000)
ty = float(4000)
tc = float(3000)


results = []

#Equações
tx1 = (tx+ty)/2 + m.sqrt(pow((tx-ty)/2,2) + pow(tc,2))
tx2 = tx + ty - tx1
tc1 = (tx1-tx2)/2
tmed = (tx+ty)/2

#Plano principal de tensão normal
angx2t = m.atan(2*tc/(tx-ty))
ang = angx2t/2

#Plano principal de tensão de cisalhamento
ang2xc = m.atan((ty-tx)/(2*tc))
ang2 = ang2xc/2

#Conferência
a = ang
tx1teste = (tx+ty)/2 + (tx-ty)*m.cos(2*a)/2 + tc*m.sin(2*a)
if tx1 == tx1teste:
    print('A tensão 1 é a máxima')
else:
    print('A tensão 2 é a máxima')

#Adionar resultados na lista de resultados
results.append(tx1)
results.append(tc1)
results.append(tx2)
results.append(tmed)
results.append(ang)
results.append(ang2)
results.append(tx1teste)

print(f'A tensão normal 1 é {results[0]}')
print(f'A tensão de cisalhamento é {results[1]}') 
print(f'A tensão normal 2 é {results[2]}')    
print(f'A tensão média no cisalhamento é {results[3]}') 
print(f'O plano principal normal é {results[4]}') 
print(f'O plano principal de cisalhamento é {results[5]}')
print(f'A tensão máxima é {results[6]}')