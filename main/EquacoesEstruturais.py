"""
! Revisar este projeto como um todo
! Vale analisar se a classe está coerente com o propósito dela
"""

import math as m

class Geometria():

    def __init__(self,geometria: str,a:float,b:float):   

        """Cria uma geometria
        :geometria = [retangulo,circulo]
        """

        self.r= geometria

        if self.r == 'retangulo':
            self.a = a
            self.b = b

        if self.r == 'circulo':
            self.raioexterno = a
            self.raiointerno = b


    def centrodegravidade(self,centrodegravidade:list):
        
        """Define o centro de gravidade para a geometria formada por diversas figuras
        :centrodegravidade = [lista com centros]
        """

        if self.r == 'retangulo':
            sumarea = 0
            cgx = 0
            cgy = 0
            for i in range(len(self.centrodegravidade))
            area = self.a[i]*self.b[i]
            sumarea = area + sumarea

            cx = self.cg[i][0]*area[i]
            cy = self.cg[i][1]*area[i]
            cgx = cx + cgx
            cgy = cy + cgy
            
            centro = (cgx/sumarea,cgy/sumarea)
        
        if self.r == 'circulo':
            sumarea = 0
            cgx = 0
            cgy = 0

            for i in range(len(self.cg)):

                if self.b:
                    area = m.pi*m.pow(self.a[i]-self.b[i],2)
                    sumarea = area + sumarea

                    cx = self.cg[i][0]*area[i]
                    cy = self.cg[i][1]*area[i]
                    cgx = cx + cgx
                    cgy = cy + cgy
                else:
                    area = m.pi*m.pow(self.a[i],2)
                    sumarea = area + sumarea

                    cx = self.cg[i][0]*area[i]
                    cy = self.cg[i][1]*area[i]
                    cgx = cx + cgx
                    cgy = cy + cgy

            centro = (cgx/sumarea,cgy/sumarea)

        return centro
                
    def momentodeinercia(self,cg=[]):

        """
        Calcula o momento de uma geometria com dimensoes especificadas e do seu centro 
        de gravidade
        """
        
        if self.cg:
            if self.r == 'r':
                iy = 0
                ix = 0

                for i in len(self.cg):
                    area = self.a[i]*self.b[i]
                    mix = (self.b[i]*m.pow(self.a[i],3)/12) + m.pow(area*(cg[i][0] - self.cg[i][1]),2)
                    miy = (self.a[i]*m.pow(self.b[i],3)/12) + m.pow(area*(cg[i][1] - self.cg[i][0]),2)
                    
                    iy = miy+iy
                    ix = mix+ix
            
            if self.r == 'c':
                pass

            else:
                print('Faltou digitar a geometria')
                pass

        else:
            for i in range(len(self.a)):
                if self.r == 'r':
                    iy = (self.b[i]*m.pow(self.a[i],3)/12)
                    ix = (self.a[i]*m.pow(self.b[i],3)/12)
                
                if self.r == 'c':
                    pass

                else:
                    print('Faltou digitar a geometria')
                    pass
            
        

        return (ix,iy)

