for i in ["karen","Copara",2]:
    print("Hola", end=" ")

for j in "karencoparagarcia@gmail.com":
    print("hola" , end="")

contador=0
miEmail=input("Introduce tu email: ")
for k in miEmail:
    #recorrido
    if (k == "@" or k=="."):
        contador=contador+1

if contador==2:
    print("email correcto")
else:
    print("incorrecto")