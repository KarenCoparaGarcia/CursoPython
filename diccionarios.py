midiccionario={"Alemania" : "Berlín", "Francia":"París","Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"])

#agregar mas elementos a un diccionario

midiccionario["Italia"]="Lisboa"
print(midiccionario)

#modificar elemento 
midiccionario["Italia"]="Roma"
print(midiccionario)

#eliminar elemento

del midiccionario["Reino Unido"]
print(midiccionario)

midiccionario1={"Alemania":"Berlín",23:"Jordan","Mosqueteros":3}
print(midiccionario1)

#añadiendo una tupla
mitupla=["España","Francia","Reino Unido","Alemania"]
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(midiccionario2["Francia"])


#asignando claves a los diccionarios
midiccionario3={23:"Maria","Nombre":"Sandra","Equipo":"Liga","anillos":[1991,1990,1998,2000]}
print(midiccionario3["anillos"])
print(midiccionario3.keys())
#imprimir claves
print(midiccionario3.values())
print(len(midiccionario3))