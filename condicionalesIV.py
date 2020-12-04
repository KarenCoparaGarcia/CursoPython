print("Programa de becas año 2020")

distancia_escuela=float(input("Introduce la distancia a la escuela en KM: "))
print(distancia_escuela)

numero_hermanos=int(input("introduce el numero de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Ingrese el salario anual bruto: "))
print(salario_familiar)

#condicional que evalue 

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("tienes derecho a beca")
else:
    print("No tienes derecho a beca")

