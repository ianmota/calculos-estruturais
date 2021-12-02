import math

class Deformacoes():
    def __init__(self) -> None:
        pass
        """
        Calcula as deformações resultantes de tensões
        em planos inclinados"""
    
    def deformacaox1(self, 
        deformacaox = 0,
        deformacaoy = 0,
        deformacaoxy = 0,
        angulo = 0
        ) -> dict:
        """Calcula a deformação em um plano inclinado
        x angulos"""

        dx = ((deformacaox+deformacaoy)/2
        + (deformacaox-deformacaoy)*math.cos(math.radians(2*angulo))/2 
        + deformacaoxy*math.sin(math.radians(2*angulo))/2)
            
        resultados = {
            'Deformação em x':format(dx,'.3E')
        }

        return resultados

    def deformacaoy1(self,dx,dy,dx1=0,ang = 0) -> dict:
        """Calcula a deformação em y no plano
        inclinado"""

        dy = dx+dy-dx1
        
        return {'A deformação em y é':format(dy,'.3E')}

    def deformacaox1y1(self,
        deformacaox,
        deformacaoy,
        deformacaoxy,
        angulo) -> dict:
        """Calcula a deformação de cisalhamento no plano
        inclinado"""

        dxy = 2*((deformacaoy-deformacaox)*math.sin(
        math.radians(2*angulo)
        )/2
        +deformacaoxy*math.cos(math.radians(2*angulo))/2)

        return {'Deformação de cisalhamento':
            format(dxy,'.3E')}

    def deformacoesprincipais(self,
        dx,
        dy,
        dxy) -> dict:
        """Define as deformações principais
        no plano inclinado"""

        df1 = ((dx+dy)/2+math.sqrt((
            math.pow((dx-dy)/2,2) + math.pow(dxy/2,2)
        )))

        df2 = dx+dy-df1

        planp = math.atan(dxy/(dx-dy))/2

        dfmax = max(df1,df2)
        dfmin = min(df1,df2)

        return {
            'Deformação fletora máxima': format(dfmax,'.3E'),
            'Deformação fletora mínima': 
                format(dfmin,'.3E'),
            'Ângulo do plano principal': 
                math.degrees(planp)
        }

    def cisalhamentoprincipal(self,
        dx,
        dy,
        dxy) -> dict:
        """Define as deformações no plano de
        cisalhamento principal"""

        dxymax = 2*math.sqrt(
            math.pow((dx-dy)/2,2) + math.pow(dxy/2,2)
        )

        #Cálculo da tensão média normal no plano
        dmed = (dx+dy)/2

        #Calculo do ângulo do plano
        if dxy:
            planp = math.atan((dx-dy)/dxy)/2
        if not dxy:
            a = Deformacoes.deformacoesprincipais(self,dx,dy,dxy)
            ang = a['Ângulo do plano principal']
            t1 = ang+45
            t2 = ang-45

            c = Deformacoes.deformacaox1y1(self,dx,dy,dxy,t1)
            d = Deformacoes.deformacaox1y1(self,dx,dy,dxy,t2)

            def1 = c['Deformação de cisalhamento']
            def2 = d['Deformação de cisalhamento']

            planp = float(max(def1,def2))
        
        return {
            'Deformação de cisalhamento máxima': format(
                dxymax,'.3E'
            ),
            'Deformação média': format(dmed,'.3E'),
            'Plano principal de cisalhamento':
            math.degrees(planp)
        
        }

    def defpoisson(self,
        dx,dy,v) -> dict:
        """Calcula as deformações levando em consideração
        o coeficiente de poisson"""

        dfx = dx - v*dy
        dfy = dy - v*dx
        dfz = v*(dx+dy)

        return {
            'Deformação em x': format(dfx,'.2E'),
            'Deformação em y': format(dfy,'.2E'),
            'Deformação em z': format(dfz,'.2E')
        }

    def poisson(self,dx,dy,tx,ty) -> float:
        """Define o coeficiente de Poisson a partir
        das deformações e tensões do elemento"""

        v = (ty*dx-tx*dy)/(tx*dx-ty*dy)
        
        return v

    def elasticidade(self,ty,tx,v=0,dx=0,dy=0) -> float:
        """Define a elasticidade a partir do coeficiente
        de Poisson"""
        try:
            if v:
                if dy:
                    e = (ty-v*tx)/dy
                if dx:
                    e = (tx-v*ty)/dx
            if not v:
                v = Deformacoes.poisson(self,dx,dy,tx,ty)
                e = (ty-v*tx)/dy
            return e
        except:
            return print('Não foi possível calcular, provavelmente '
            'você não digitou o coeficiente ou algum outro'
            ' parâmetro')

    def tensoes(self, dy,elasticidade,
        v,dx,) -> float:
        """Define a deformação em um elemento a partir da
        deformação que ele apresenta"""

        tx = (dy*elasticidade*v+dx*elasticidade)/(1-v**2)

        ty = dy*elasticidade + v*tx

        return tx,ty    
