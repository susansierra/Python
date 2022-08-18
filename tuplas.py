tupla = ('juan','1/1/200', 123)
print(tupla)
print(type(tupla))

#acceder
print(f"El primer elemento de la tupla es {tupla[0]}")
print(f"El tercer elemento de la tupla es {tupla[2]}")
print(f"El tamaño de la tupla es {len(tupla)}")

#crear
tupla= (('juan','1/1/2000',123),('pedro','1/2/2000',456))
print(tupla)
print(type(tupla))  

#acceder 
tupla = (('juan','1/1/2000',123),('pedro','1/2/2000',456))
print(f"El 1er elemento es {tupla[0]}")
print(f"El 2do elemento del primer item es {tupla[0][1]}")
print(f"El tamaño de la tupla es {len(tupla)}")
print(f"El tamaño del 2do elemento es {len(tupla[1])}")