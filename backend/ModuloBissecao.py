import math as m

def funcao(x):
         
    return x + 3*m.cos(x) - m.pow(m.e,x)

class Bissecao():

    """Para cálculo de raizes através do método de bisseção"""

    def __init__(self, a, b, precisao):

        self.a = a
        self.b = b
        self.precisao = precisao
    
    def media(self):

        return  (self.a + self.b)/2

    def erropadrao(self):

        x = self.media()
        return m.fabs(self.a - x)

    def errorelativo(self):

        x = self.media()
        return m.fabs(( self.a - x) / x)
    
    def erroabsoluto(self):

        x = self.media()
        return m.fabs(funcao(x)) < self.precisao


def calculo_de_raiz_a(x, a):
    
    if funcao(x) > 0 and funcao(a) > 0:

        a = x

    if funcao(x) < 0 and funcao(a) < 0:

        a = x

    return a
    
def calculo_de_raiz_b(x, b):

    if funcao(x) > 0 and funcao(b) > 0:

        b = x

    if funcao(x) < 0 and funcao(b) < 0:

        b= x

    return b

    
   
    

        

