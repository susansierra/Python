#iteradores 

lista1 = [1,2,3,4,5]
for i in lista1:
    print(i, end="|")

print("")

iter1 = iter(lista1)
for i in iter1:
    print(i, end=",")

print("")

enum1 = enumerate(lista1)
print(next(enum1))
print("")