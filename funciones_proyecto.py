print ("Para 4 integrantes recolecta 4 elementos sin importar las cantidades y las adiciones en las mochilas")
brujula = 60.99
linterna_funcional = 29.99
snacks = 8.8
agua_en_botella = 11.30

def calculartotalelementosenmochila(vehiculo):
    totalelementos = {}
    print("Calculo en tu mochila")
    for mochila in vehiculo:
        for elemento, detalle in mochila.items():
            if elemento in totalelementos:
                totalelementos[elemento] += detalle
            else:
                totalelementos[elemento] = detalle
    print(totalelementos)

def imprimir(estructura):
    for objeto in estructura:
        print(objeto)

vehiculo = [{}] * 4

for i in range(4):
    vehiculo[i] = {
        "brujula" :  brujula,
        "linterna_funcional" : linterna_funcional,
        "snacks" : snacks,
        "agua_en_botella" : agua_en_botella
    }
    imprimir(vehiculo)
    calculartotalelementosenmochila(vehiculo)

