"""Upgrades 
- Implantação do pivoteamento parcial
- Matrizes captadas do excel
LEMBRAR DE FAZER CÓPIA DO ARQUIVO FDP"""

import numpy

#matrizes
k11= 3
k12 = 0.5
k13 = 0.25
k22 = 2
k23 = 0.5
k33 = 1.75
a = 0
b = 0
c = -4.25

matriz_rigidez = numpy.array([[k11,k12,k13],
                              [k12,k22,k23],
                              [k13,k23,k33]
                             ])

vetor_deformacao = numpy.array([[a],
                                [b],
                                [c]
                                ])

                            
#Eliminação de Gauss - VERIFICADO
for i in range(len(matriz_rigidez)-1):
    for k in range(i+1,len(matriz_rigidez)):

        m = float(matriz_rigidez[k][i]/matriz_rigidez[i][i])
        matriz_rigidez[k][i] = 0


        for j in range(i+1,len(matriz_rigidez)):
            matriz_rigidez[k][j] = matriz_rigidez[k][j] - m*matriz_rigidez[i][j]

        vetor_deformacao[k] = vetor_deformacao[k] - m*vetor_deformacao[i]

#Resolução da equação
vetor_forca = numpy.zeros(len(matriz_rigidez))
for i in range(len(matriz_rigidez)-1,-1,-1):
    c = 0

    for k in range(len(matriz_rigidez)-1,i,-1):
        c_ = float(matriz_rigidez[i][k]*vetor_forca[k])
        c += c_
  

    if i == (len(matriz_rigidez)-1):
        x = vetor_deformacao[i]/matriz_rigidez[i][i] 
        vetor_forca[i] = x
        
    else:
        x = (vetor_deformacao[i] - c)/matriz_rigidez[i][i]
        vetor_forca[i] = x

for i in range(len(vetor_forca)):
    print(f'x{i} = {vetor_forca[i]}')

    






    
        
    
    






