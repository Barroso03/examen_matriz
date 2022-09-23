# examen_matriz
El link de mi repostorio es:()


MAIN.PY:
'''
from prueba import *
from tabla import *
devuelvematriz(matriz)
escribetexto()
printarlistas()
dar_valores( 3,2)
'''
PRUEBA.PY:
'''
matriz = [[1, 1, 1, 3],[2, 2, 2, 7], [3, 3, 3, 9],[4, 4, 4, 13]]



def devuelvematriz(matriz):
  for i in matriz:
      lista = []
      lista.append(i)
      if lista[0][0]+lista[0][1]+lista[0][2]== lista[0][3]:
          print(lista)
      else:
          cuatro = lista[0][0]+lista[0][1]+lista[0][2]
          print([lista[0][0],lista[0][1],lista[0][2],cuatro])
devuelvematriz(matriz)       


def escribetexto():
   texto=input("Introduce cadena:")
   if len(texto) >=3 and len(texto) <= 10:
    print(True)
   else:
    print(False)
escribetexto()






def printarlistas():

   print([i for i in range(0,11)])
   print([i for i in range(-10,1)])
   print([i for i in range(0,21) if i%2==0])
   print([i for i in range(-20,1) if i%2!=0])
   print([i for i in range(0,51) if i%5==0])
   print([i for i in range(0,11)])
printarlistas()
'''
TABLA.PY:
'''
def dar_valores(n,m):
    if n >= 1 and n <= 9 and m >= 1 and m <= 9: 
        print (n,m)
    else:
        print("Introduce otros valores correctos")
    for i in range(n):
        for j in range(m):
            print(" * ", end='')
'''
