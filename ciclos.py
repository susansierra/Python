numero = int(input("digite un numero"))

while numero < 20:
    numero +=1 
    print("numero",numero)

numero_pasos = int(input("¿Cuantos pasos vas a dar?"))
for i in range(0, numero_pasos + 1, 1):
    print("Estas en el paso", i)