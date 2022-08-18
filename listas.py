list_example_one = [8,'python',True,'texto',20.1,10.3]
list_example_two = list([8,'python',True,'texto',20.1,10.3])

print("[]",type(list_example_one),list_example_two)
print("list()",type(list_example_one),list_example_two)

#Indices 

print("Posicion 2:",list_example_one[2])
print("Ultima posicion 2:",list_example_one[-1])

#Append inserta una lista
#Extend extiende una lista

list_example_one.append([4,"Hola"])
print("Append:", list_example_one)

list_example_one.extend([4,"Hola"])
print("Extend:", list_example_one)

#accion eliminar
#remove indica que valor de la lista quieres eliminar
#pop indica en posicion de la lista quieres eliminar

print("antes", list_example_one)
list_example_one.remove(20.1)
print("Despues:",list_example_one)

print("antes", list_example_one)
list_example_one.pop(2)
print("Despues:",list_example_one)