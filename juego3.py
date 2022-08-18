print("La esfingue le hizo una actualización a tu mochila, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras  el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenar")

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

#forma de hacerlo con tuplas
mochila = (
    ("linterna_y_bateria",1,linterna_y_bateria),
    ("agua_en_botella",2,agua_en_botella),
    ("snacks",3,snacks)
)

print("Tienes actualmente",len(mochila),"objetos")

for x,y,z in mochila:
    print("Tienes",y,x,"que tiene el valor de",z)

#forma de hacerlo con diccionarios

mochila = {
    "agua_en_botella" : {
        "cantidad" : 1,
        "valor_unitario" : agua_en_botella
    },
    "linterna" : {
        "cantidad" : 1,
        "valor_unitario" : linterna
    },
    "brujula" : {
        "cantidad" : 1,
        "valor_unitario" : brujula
    },
}

for i,j in mochila.items():
    print(i,j)

print("En esta aventura te van a acompañar 8 integrantes más, y te han pedido que les armes una mochila igual a la tuya y la coloques en el vehiculo")

vehiculo = [{}] * 8

for i in range(8):
    vehiculo[i] = {
        "agua_en_botella" : {
        "cantidad" : 1,
        "valor_unitario" : agua_en_botella
    },
    "linterna" : {
        "cantidad" : 1,
        "valor_unitario" : linterna
    },
    "brujula" : {
        "cantidad" : 1,
        "valor_unitario" : brujula
    }
    }
    print("Acabas de armar la mochila para el compartimiento" , i + 1)

