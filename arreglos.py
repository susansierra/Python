
import array


array_example = array.array("i", [1,2,3,4,5])

print(array_example)
print(type(array_example))

print("el primer elemento es:", array_example[0])
print("el primer elemento es:", array_example[-1])

#insertar elementos en los arreglos
array_example.insert(5,6)
print(array_example)

#modificar elementos en los arreglos
array_example[0] = 10
print(array_example)

#concatenar
array_example_one = array.array("i", [1,3,4,8,9])
array_example_two = array.array("i", [7,5,0,1,2,6,7])
print(array_example_one + array_example_two)

#elementos
print("before pop:", array_example_one)
print("value eliminated:", array_example_one.pop())
print("after pop:", array_example_one)


print("before pop:", array_example_one)
print("value eliminated:", array_example_one.pop(3))
print("after pop:", array_example_one)