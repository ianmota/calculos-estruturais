import numpy as np
from numpy.linalg import norm
from scipy.linalg import eigh
import matplotlib.pyplot as plt

def configuração():
   # Definição do sistema de coordenadas:
   eixo_x = np.array([1,0])
   eixo_y = np.array([0,1])

   # Definição do modelo:
   nós              = { 1:[0,10], 2:[0,0], 3:[10,5]}
   graus_de_liberdade = { 1:[1,2], 2:[3,4], 3:[5,6] }
   elementos        = { 1:[1,3], 2:[2,3] }
   gl_restringidos    = [1, 2, 3, 4] #graus de liberdade restringidos
   forças             = { 1:[0,0], 2:[0,0], 3:[0,-200] }

   # Propriedades do material - aço AISI 1095:
   densidades   = {1:0.284, 2:0.284} #lb/in³
   rigidezes = {1:30.0e6, 2:30.0e6}  #lb

   # Propriedades geométricas:
   áreas = {1:1.0, 2:2.0}  #in²

   ngl = 2 * len(nós)  #número total de graus de liberdade do sistema

   # Hipóteses:
   assert len(densidades) == len(elementos) == len(rigidezes) == len(áreas)
   assert len(gl_restringidos) < ngl
   assert len(forças) == len(nós)

   return {  'eixo_x':eixo_x, 'eixo_y':eixo_y, 'nós':nós, 'graus_de_liberdade':graus_de_liberdade,   \
            'elementos':elementos, 'gl_restringidos':gl_restringidos, 'forças':forças, 'ngl':ngl,     \
            'densidades':densidades, 'rigidezes':rigidezes, 'áreas':áreas }

def plotar_nós(nós):
   x = [i[0] for i in nós.values()]
   y = [i[1] for i in nós.values()]
   tamanho = 400
   offset = tamanho/4000.
   plt.scatter(x, y, c='y', s=tamanho, zorder=5)
   for i, local in enumerate(zip(x,y)):
      plt.annotate(i+1, (local[0]-offset, local[1]-offset), zorder=10)


def pontos(elemento, propriedades):
   elementos = propriedades['elementos']
   nós = propriedades['nós']
   graus_de_liberdade = propriedades['graus_de_liberdade']

   # Relacionamento dos nós aos respectivos elementos:
   do_nó = elementos[elemento][0]
   para_o_nó = elementos[elemento][1]

   # Determinando as coordenadas de cada nó:
   do_ponto = np.array(nós[do_nó])
   para_o_ponto = np.array(nós[para_o_nó])

   # Determinando os graus de liberdade para cada elemento:
   gl = graus_de_liberdade[do_nó]
   gl.extend(graus_de_liberdade[para_o_nó])
   gl = np.array(gl)

   return do_ponto, para_o_ponto, gl

def desenhe_elemento(do_ponto, para_o_ponto, elemento, áreas):
   x1 = do_ponto[0]
   y1 = do_ponto[1]
   x2 = para_o_ponto[0]
   y2 = para_o_ponto[1]
   plt.plot([x1, x2], [y1, y2], color='g', linestyle='-', linewidth=7*áreas[elemento], zorder=1)

def cosseno_diretor(vet1, vet2):
   return np.dot(vet1,vet2) / (norm(vet1) * norm(vet2))

def matriz_de_rotação(vetor_do_elemento, eixo_x, eixo_y):
   # Obtendo os cossenos diretores:
   proj_x = cosseno_diretor(vetor_do_elemento, eixo_x)
   proj_y = cosseno_diretor(vetor_do_elemento, eixo_y)
   return np.array([[proj_x,proj_y,0,0],[0,0,proj_x,proj_y]])

def obtém_matriz(propriedades):
    # Construção da matriz de rigidez global:
   ngl    = propriedades['ngl']
   nós    = propriedades['nós']
   elementos = propriedades['elementos']
   forças   = propriedades['forças']
   áreas    = propriedades['áreas']
   eixo_x   = propriedades['eixo_x']
   eixo_y   = propriedades['eixo_y']

   plotar_nós(nós)
   K = np.zeros((ngl,ngl))
   for elemento in elementos:
        # Determinar a geometria do elemento:
      do_ponto, para_o_ponto, gl = pontos(elemento, propriedades)  #gl = graus de liberdade
      vetor_do_elemento = para_o_ponto - do_ponto

        # Mostrando o elemento
      desenhe_elemento(do_ponto, para_o_ponto, elemento, áreas)

      # Obtendo as matrizes de massa e rigidez o elemento:
      comprimento = norm(vetor_do_elemento)
      área   = propriedades['áreas'][elemento]
      E      = propriedades['rigidezes'][elemento]

      Ck = E * área / comprimento

      k = np.array([[1,-1],[-1,1]])

      # Obtendo as matrizes de massa e rigidez rotacionadas do elemento:
      tau = matriz_de_rotação(vetor_do_elemento, eixo_x, eixo_y)
      k_r = tau.T.dot(k).dot(tau)

      # Trocando das coordenadas do elemento para as coordenadas globais
      índice = gl-1
      B = np.zeros((4,ngl))
      for i in range(4):
         B[i,índice[i]] = 1.0
      K_rG = B.T.dot(k_r).dot(B)
      K += Ck * K_rG

   # Construindo o vetor de forças:
   F = []
   for f in forças.values():
      F.extend(f)
   F = np.array(F)

   # Removendo os graus de liberdade restringidos:
   remove_índices = np.array(propriedades['gl_restringidos']) - 1

   for i in [0,1]:
      K = np.delete(K, remove_índices, axis=i)

   F = np.delete(F, remove_índices)

   return K, F

def obtém_tensões(propriedades, X):
   eixo_x   = propriedades['eixo_x']
   eixo_y   = propriedades['eixo_y']
   elementos = propriedades['elementos']
   E      = propriedades['rigidezes']

   # Obtendo as tensões em cada elemento:
   tensões = []
   for elemento in elementos:
      # Determinar a geometria do elemento:
      do_ponto, para_o_ponto, gl = pontos(elemento, propriedades)
      vetor_do_elemento = para_o_ponto - do_ponto

      # Obtendo a matriz de rotação:
      tau = matriz_de_rotação(vetor_do_elemento, eixo_x, eixo_y)
      deslocamentos_globais = np.array([0,0,X[0],X[1]])
      deslocamento_nodal = tau.dot(deslocamentos_globais)

      # Cálculo das tensões e das deformações:
      deformação = (deslocamento_nodal[1] - deslocamento_nodal[0]) / norm(vetor_do_elemento)
      tensão = E[elemento] * deformação
      tensões.append(tensão)

   return tensões

def mostra_resultados(X, tensões):
   print ('Deslocamentos Nodais:', X)
   print ('Tensões', tensões)
   print ('Magnitude do Deslocamento:', round(norm(X),5))

def corpo():
   # 1)Configuração do problema
   propriedades = configuração()

   # 2)Determinar a matriz global
   K, F = obtém_matriz(propriedades)

   # 3)Calcular os deslocamentos de cada elemento
   X = np.linalg.inv(K).dot(F)

   # 4)Calcular as tensões em cada elemento
   tensões = obtém_tensões(propriedades, X)

   # 5)Plotagem dos resultados
   mostra_resultados(X, tensões)

   plt.title('Análise da Treliça')
   plt.show()
if __name__ == '__main__':
   corpo()
