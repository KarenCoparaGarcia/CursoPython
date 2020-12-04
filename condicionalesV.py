print("Asignaturas Optativas")
print("Asignaturas Optativas: Informatica grafica - Pruebas de Software -Usabilidad y accesibilidad")
opcion=input("Escriba la asginatura escogida: ")
asignatura=opcion.lower()
if asignatura in ("informatica grafica" ,"pruebas de software" ,"usabilidad y accesibilidad"):
    print("Asignatura elegida "+ asignatura)
else:
    print("La asignatura escogida no esta en el listado.")   
