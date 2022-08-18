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

print("No debes colocar mas de 5 objetos en tu mochila y tampoco te pases de los 200 trekjuls")

mochila = 0 

if agua_en_botella + linterna_y_bateria + reloj <= 200:
    print("Se pudo colocar los objetos con exito")
else:
    print("No se pudo colocar los obejtos")

print("Es tu dia de suerte! te avoy a dar otra mochila, pero solo puedes agregarle agua en botella")

mochila2 = 0 
while (mochila2 + agua_en_botella <= 200):
    mochila2 +=agua_en_botella
    print("Haz podido agregar: ", mochila2)