#Un bucle while en Python repite un bloque de código mientras
# una condición sea verdadera (True).
# Deja de ejecutarse en cuanto la condición pasa a ser falsa (False).


#Mientras it sea mayor que 1
#Imprímelo, result: ciclo infinito
it = 4

#while it>1:
#    print(it)

#Mientras it sea mayor que 1
#Imprímelo,
#Pero hazlo de forma descendiente
while it>1:
    print(it)
    it=it-1

#Mientras it sea mayor que 1
#Imprímelo, pero si el numero
#Es igual a 3 ,entonces finaliza
#el código
while it>1:
    if it==3:
        break
    print(it)
