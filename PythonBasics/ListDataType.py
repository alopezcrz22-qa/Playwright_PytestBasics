#Las lista en python son colecciones ordenadas
# y mutables (que se pueden modificar), delimitadas por corchetes []

#Definir una lista
values = [1, 2, "Alan", "Lopez", 5.0]
#Imprimimos un valor de dicha lista
print(values[0]) #[0] = 1
#Imprimimso el ultimo elemento de la lista
print(values[-1]) #[-1] = 5.0
#Imprimos los valores desde 1 al 3 de la lista
print(values[1:3]) #[1:3] = 2, 'Alan'

#Agregamos un valor a esa lista en una poscion en especifico
values.insert(6, "John")
print(values)

#Agregamos un valor en la ultimas posicion de la lista
values.append("Last")
print(values)

#Modificamos un elemento de una psicion en especifico
values[2] = "Angela"
print(values)

#Eliminamos un elemrnto de una posicion en especifico
del values[0]
print(values)


##############Exercises

fruits=['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f'First fruit: {fruits[0]}')
print(f'Last fruit: {fruits[-1]}')

print(f'Fruits from index 1 to 1: {fruits[1:3]}')
