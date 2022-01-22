import numpy


class MetodoDeGauss():
    def __init__(self,b:list,z:list):
        """Esta classe serve para calcular qualquer sistema linear utilizando 
        o método de gauss por pivoteamento parcial

        Args:
            b (list): Matriz de rigidez na forma de lista com os números em ordem
            z (list): Vetor força na forma de lista com os números em ordem
        """
        self.b = b
        self.z = z
        self.matriz_calculation()
        
    def matriz_rigidez(self,n:int):
        """Monta a matriz de rigidez no pórtico

        Args:
            n (int): Determina o eixo da matriz quadrada
            b (float, optional): Coeficientes de rigidez no formato de lista

        Returns:
            Matriz de rigidez no formato necessário de cálculo
        """
        matriz = numpy.array(self.b,dtype=numpy.float64)
        matriz_rigidez = matriz.reshape(n,n)
        return matriz_rigidez

    def vetor_deformacao(self):
        """Monta o vetor de deformação do pórtico

        Args:
            b (float, optional): Vetores de deformação no formato de lista

        Returns:
            O vetor de deformação no formato necessário para os cálculos
        """
        vetor_deformacao = numpy.array(self.z,dtype=numpy.float64)
        return vetor_deformacao

    def metodo_de_gauss(self,matriz_rigidez,vetor_deformacao):
        """Calcula a matriz de rigidez e as deformações do pórtico

        Args:
            matriz_rigidez ([type]): Matriz no formato fornecido pela função matriz_rigidez()
            vetor_deformacao ([type]): Vetor no formato fornecido pela função vetor_deformacao()
        """
        nmax = matriz_rigidez[0][0]
        u = 0
        for i in range(len(matriz_rigidez)-1):
            
            #Calcula o pivoteamento parcial
            for t in range(i+1,len(matriz_rigidez)):
                if matriz_rigidez[t][i]>nmax:
                    nmax = matriz_rigidez[t][i]
                    matriz_rigidez[[u,t]] = matriz_rigidez[[t,u]]
                    vetor_deformacao[[u,t]] = vetor_deformacao[[t,u]]
                    u = t

            #Calcula a matriz triangular
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

        return vetor_forca

    def matriz_calculation(self): 
        """Função utilizada para chamar todas as outras funções em ordem e consequentemente calcular

        Returns:
            float: Resultado do sistema linear
        """
        x = self.matriz_rigidez(int(len(self.b)**0.5))
        y = self.vetor_deformacao()
        return self.metodo_de_gauss(x,y)







