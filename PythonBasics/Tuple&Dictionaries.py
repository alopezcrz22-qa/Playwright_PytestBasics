#Tupla
# en Python es una estructura de datos ordenada
# e inmutable (de solo lectura), lo que significa que sus elementos no se pueden modificar
# agregar ni eliminar una vez que ha sido creada.
val=(1,2,"Alan",4.5)
print(val)

#En este caso generaria un error
#val[2] = "RAHUL" #TypeError: 'tuple' object does not support item assignment

#Dictionary
#en Python es una estructura de datos mutable que almacena información
# en pares de clave y valor (key: value), permitiendo buscar elementos rápidamente
# mediante su clave en lugar de usar un índice numérico.
dic = {'apple':'orange', 'banana':'strawberry', 'c':3, 'd':4}
print(dic)
#De la siguiente forma definimos un diccionario vacio para despues agregar elementos
dic2= {}
dic2['apple']='orange'
dic2['banana']='strawberry'
print(dic2)
#Imprimimos el valor del diccionario o significado
print(dic2["apple"])

#De la siguiente forma podemos actualizar un valor del diccioanrio
dic2["apple"]='apple'
dic2["banana"]='banana'
print(dic2)

