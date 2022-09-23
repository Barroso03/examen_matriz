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





        


