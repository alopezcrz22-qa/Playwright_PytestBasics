#For Loop
# se utiliza para recorrer los elementos de un objeto iterable
# (como una lista, una tupla, un diccionario, una cadena de texto o un rango numérico)
# y ejecutar un bloque de código para cada uno de ellos

#Creamos una lista
obj = [2, 3, 5, 7, 9]
#iteramos sobre el elemento definiendo un identificador
# itera i en tu lista
#La variable i actúa como un contenedor temporal
# (puedes nombrarla como quieras, pero i es una convención muy común que viene de ítem).
for i in obj:
    #y realiza una accion
    print(i*2)

############################################################################3
#La función range(1, 6) genera una secuencia de números que empiezan en el 1
# y terminan antes del 6 (es decir, genera los números: 1, 2, 3, 4 y 5).
# El ciclo for tomará cada uno de estos números y los asignará a i uno por uno.
sum = 0
for i in range(1, 6):
    #En cada vuelta, toma lo que ya tenía acumulado en sum, le suma el valor actual de i
    sum = sum + i
print(f'La suma es: {sum}')

############################################################################3
#Inicia el ciclo desde 0 hasta el num 10
#ya que en este caso no asignamos un valor como (1, 10)
for k in range(10):
    print(k)

###########################################################################
#Inicia el ciclo desde 1 hasta el num 10
#pero en esta ocasion da saltos de 5 en 5
#es decir imprimira el 1, 6 {1 mas 5= 6 }
for m in range(1, 10, 5):
    print(f'El salto de 5 en 5:{m}')