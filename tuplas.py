mitupla=("Juan",12,1,1992)
milista=list(mitupla)
print(mitupla)

#tupla es con parentesis y listas es con corchetes.

milista2=["maria",12,1,4]
mitupla2=tuple(milista2)
print(milista2)

print("maria" in mitupla2)

#cuantas veces se encuentra el elemento
print(mitupla2.count(14))
print(len(mitupla2))

#tupla sin parentesis, empaquetado de tuplas
mitupla3="juanito",10,11,2020
#desempaquetado de tuplas
nombre, dia, mes, agno= mitupla3
print(nombre)
print(dia)
print(mes)
print(agno)

