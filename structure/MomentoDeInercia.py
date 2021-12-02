#Importações
import math as m
import pandas as pd
import openpyxl as op


#Variáveis alteráveis
altura = [0.4]
largura = [0.20]
cggeral = 0
cg = []
elaste = 2*m.pow(10,7)
dfnormal = [-7,7.11]
dfmomento = [-472.5,245.33]
dftxt = ['deformação 10','deformação 11']

#Variáveis de operação
deforg = []

#Equações/Verificações

if not cggeral:
    cggeral = 0
    cg.append(0)
    
    for i in range(len(altura)):

        arearet = largura[i]*altura[i]
        inerciaret = (largura[i]*m.pow(altura[i],3)/12)+arearet*m.pow(cggeral-cg[i],2)
        moduloea = elaste*arearet

modulorigidez = elaste*inerciaret

for i in range(len(dfnormal)):
    deforgx = (dfnormal[i]/moduloea) + (dfmomento[i]/modulorigidez)
    deforg.append(deforgx)

forca = -deforg[0]/deforg[1]
x = []


"""
#Código
for i in range(len(dfnormal)):
    print(f'A {dftxt[i]} é {deforg[i]}')
"""
