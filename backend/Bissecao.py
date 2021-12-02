import math as m
from module_bissecao import Bissecao, funcao, calculo_de_raiz_a, calculo_de_raiz_b

a = float(input('Inicio do intervalo:\n'))
b = float(input('Fim do intervalo:\n'))
precisao = float(input('Precisao para parada, em decimal:\n'))

cont = 0


while True:
    cont += 1
    objeto = Bissecao(a,b,precisao)
    x = objeto.media()

    a = calculo_de_raiz_a(x,a)
    b = calculo_de_raiz_b(x,b)
    
    if objeto.erroabsoluto():
        break

    if cont == 1001:
        print('Houve algum erro no algoritimo!!')
        break

print(f'O valor da raiz é {x}')