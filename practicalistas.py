#CLASES DE LISTAS
#ESTRUCTURA DE DATOS QUE PERMITE ALMACENAR VARIAAS VARIABLES
#nombreLista=[elem1,elem2,elem3]

miLista=["Maria","Pepe","Marta","Antonio"]
print(miLista[-2])
print (miLista[:])
print(miLista[0:3])
print(miLista[:3])
print(miLista[1:2])#excluye el primer dato
print(miLista[2:])
#miLista.append("Sandra")
#print(miLista[:])

#insertar en posicion
miLista.insert(2,"Sandra")
print(miLista[:])

#añadiendo una lista a otra lista
miLista.extend(["Ana","Miguel","Karen"])
print(miLista[:])
print(miLista.index("Antonio"))

#retorna false o true
miLista2=["Marcia",5,True,38.6]
miLista2.extend(["Samuel","Pera"])
miLista2.remove("Pera")

#elimina el ultimo elemento
miLista2.pop()
print(miLista2[:])


miLista3=["Alma",2,True,40.6]
miLista4=["Sole",1,True,55.6]
miLista5=miLista3+miLista4
print(miLista5[:])





