#Proyecto final
print("Bienvenidos a mi juego de Trekjuls")

#Parte 1 
print("Como primer avance, deberás definir mediante el uso de variables los elementos a usar para una aventura de trekking. También usarás operadores para combinar elementos.")

mapa = 70.67
botas = 12.23
bateria = 11.69
linterna = 28
agua = 73
botella = 20.5
snacks = 8.8
brujula = 60.99
reloj = 83.75
lentes_sol = 53.28
agua_en_botella = agua + botella
linterna_y_bateria = linterna + bateria

#Parte 2
print("En este segundo avance, aplicarás  condicionales y ciclos para llenar dos mochilas, cada una con diferente filtro.")

mochila1 = 0
mochila2 = 0 
#La primera mochila tendra la capacidad de 100 puntos
if ( mapa + botas + bateria) <= 100:
    mochila1 = mapa + botas + bateria
else: 
    mochila1 = mapa + botas
print("Se ha llenado la mochila 1 con", mochila1)
#La segunda mochila tendra la capacidad de 150 puntos
if ( lentes_sol + agua_en_botella + linterna_y_bateria ) <= 150:
    mochila2 = lentes_sol + agua_en_botella + linterna_y_bateria
else: 
    mochila2 = lentes_sol + agua_en_botella 
print("Se ha llenado la mochila 2 con", mochila2)

#Parte 3
print ("Como tercer punto, harás uso de los diccionarios y las listas para actualizar las mochilas y ver a detalle los elementos que contiene. Además, tendrás que lograr llenar las mochilas para un equipo de 7 personas más.")
#crear diccionario
mochila = {
    "mapa" : {
        "cantidad" : 1,
        "valor" : 70.67
    },
    "brujula" : {
        "cantidad" : 1,
        "valor" : 60.99
    },
    "reloj" : {
        "cantidad" : 1,
        "valor" : 83.75
    }
}

#actualizar las mochilas
for i,j in mochila.items():
    if i == "mapa":
       for h in j.items():
        if j == "cantidad":
            j[0] = 2

print(mochila)

#crear lista de mochilas para 7 personas
lista_mochilas = [{}] * 7
#Llenar las 7 mochilas 

for i in range(7):
    lista_mochilas[i] = {
        "mapa" : {
        "cantidad" : 1,
        "valor" : 70.67
    },
    "brujula" : {
        "cantidad" : 1,
        "valor" : 60.99
    },
    "reloj" : {
        "cantidad" : 1,
        "valor" : 83.75
    }
    }
    print("Acabas de armar la mochila para la persona numero:" , i + 1)

#Parte 4
print("En este último avance, agregarás unos cuantos elementos más a las mochilas de algunos compañeros y calcularás el total de elementos que tiene el grupo haciendo uso de las funciones.")

#Agregar elementos a las mochilas 
mochila[4] =  {"linterna" : {
        "cantidad" : 1,
        "valor" : 28
    }
}

#Calcular el total de elementos
def calculartotalelementosenmochila(lista_mochilas):
    totalelementos = {}
    print("Calculo en tu mochila")
    for mochila in lista_mochilas:
        for elemento, detalle in mochila.items():
            if elemento in totalelementos:
                totalelementos[elemento] += detalle
            else:
                totalelementos[elemento] = detalle
    print(totalelementos) 

lista_mochilas = [{}] * 7
#Llenar las 7 mochilas 

for i in range(7):
    lista_mochilas[i] = {
        "mapa" : {
        "cantidad" : 1,
        "valor" : 70.67
    },
    "brujula" : {
        "cantidad" : 1,
        "valor" : 60.99
    },
    "reloj" : {
        "cantidad" : 1,
        "valor" : 83.75
    }
    }
    calculartotalelementosenmochila(lista_mochilas)

