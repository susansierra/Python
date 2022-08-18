colores = {
    1 : "Azul",
    7 : "Verde",
    3 : "Amarillo",
    5 : "Negro",
    8 : "Rojo",
    6 : "Naranja",
    11 : "Morado"
}

print(colores)

for i,j in colores.items():
    print(i,j)

len(colores)

print(colores.keys)

print(colores.values)

colores.clear()

#adicionar elementos
colores[12] = 'Cafe'
print(colores)

#eliminar elementos 
colores.pop(5, None)

#vaciar diccionario
colores.clear()
print(colores)
