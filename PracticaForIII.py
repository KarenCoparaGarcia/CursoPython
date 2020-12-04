for i in range(5):
    print(f"valor de la variable {i}")

#evaluar range en string    
valido=False
email=input("Ingrese su email: ")

for j in range(len(email)):
    if email[j]=="@":
        valido=True

    
if email:
    print("correcto")
else:
    print("email incorrecto")