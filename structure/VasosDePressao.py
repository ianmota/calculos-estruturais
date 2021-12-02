class VasoDePressao():
    
    def __init__(self,pressao=0,espessura=0,raio=0,tensao=0):
        """Calcula as tensões presentes em vasos de pressão"""
        self.p = pressao
        self.t = espessura
        self.r = raio
        self.ten = tensao
        self.conf = ['cilindro','esfera']
    
    def tensaocircunferencial(self,geometria):
        """Define a tensão na secção longitudinal do cilindro"""

        if not self.ten: 
            if geometria == self.conf[0]:
                ten = self.p*self.r/self.t
            if geometria == self.conf[1]:
                ten = self.p*self.r/(2*self.t)

        return ten
    
    def tensaologintudinal(self,geometria):
        """Define a tensão na secção circular do cilindro (e circunferências)"""
        if not self.ten:
            if geometria == self.conf[0]:
                pre = self.p*self.r/(2*self.t)

            if geometria == self.conf[1]:
                ten = self.p*self.r/(2*self.t)

        return pre

    def tensaosupinterna(self,geometria):
        """Define a tensão de cisalhamento da geometria (cilindro ou esfera) """
        if not self.tensao:
            if geometria == self.conf[0]:
                pre = self.p*self.r/(2*self.t)
            if geometria == 'esfera':
                pre = (self.p/2)*((self.r/2*self.t+1))

        return pre        

    def tensaonasupexterna(self,geometria=''):
        """Calcula a tensão de cisalhamento da geometria (cilindro
        ou esfera) na superfície externa"""

        if geometria == 'cilindro':
            pre = self.p*self.r/(2*self.t)
        if geometria == 'esfera':
            pre = self.p*self.r/(4*self.t)

        return pre              
    
    def tensaodecisalhamento(self,geometria):
        """Calcula a tensao decisalhamento do elemento especificado"""
        
