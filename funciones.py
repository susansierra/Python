def suma(a,b =1):
    return a + b

resultado = suma(5)
print(resultado)

resultado = suma(a= 5, b= 10)
print(resultado)

#asignar una variable a una funcion 
s = suma

resultado = s(5,3)
print(resultado)

def duplicar(dato):
    dato = dato * 2

numero = 10 
duplicar(numero)
print(numero)

#pasar por referencia

def duplicar(datos):
    for i,n in enumerate(datos):
        numeros[i] = numeros[i] * 2

numeros = [10,5,2]
duplicar(numeros)
print(numeros)