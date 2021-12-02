import math as m
from module_bissecao import Bissecao, funcao

a = float(input('Inicio do intervalo:\n'))
b = float(input('Fim do intervalo:\n'))
precisao = float(input('Precisao para parada, em decimal:\n'))

cont = 0


while True:
    cont += 1
    objeto = Bissecao(a,b,precisao)
    x = objeto.media()

    if funcao(x) > 0 and funcao(a) > 0:

        a = x

    if funcao(x) < 0 and funcao(a) < 0:

        a = x

    if funcao(x) > 0 and funcao(b) > 0:

        b = x

    if funcao(x) < 0 and funcao(b) < 0:

        b= x
    
    if objeto.erroabsoluto():
        break

    if cont == 1001:
        print('Houve algum erro no algoritimo!!')

print(f'O valor da raiz é {x}')






    



