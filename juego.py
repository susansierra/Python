print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

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

print("Lista tres objetos del equipamiento: Nombre y valor")

print("botella",botella)
print("agua",agua)
print("snacks",snacks)

print("Puedes combinar elementos de tu equipo para prepararte mejor?")

agua_en_botella = agua + botella
linterna_y_bateria = linterna + bateria

print("agua en botella",agua_en_botella)
print("linterna y bateria",linterna_y_bateria)

print("El precio de agua en botella es menor al de la linterna funcional?")

validacion =  agua_en_botella < linterna_y_bateria

print("Respuesta",validacion)

print("Cuanto valdria comprar unos snacks y una brujula?")

suma = snacks + brujula 

print("valor total",suma)

print("Si tengo 100 puntos, me alcanza para comprar unas botas?")

print(botas <= 100)

