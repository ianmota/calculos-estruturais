     nmax = matriz_rigidez[t][i]
                print(nmax)
                matriz_rigidez[[u,t]] = matriz_rigidez[[t,u]]
                u = t