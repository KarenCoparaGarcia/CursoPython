print("verificacion de acceso")

nota_alumno=int(input("Introduce tu nota: "))

if nota_alumno<5:
    print("reprobado")
elif nota_alumno<6:
    print("suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("excelente")
else:
    print("Sobresaliente")