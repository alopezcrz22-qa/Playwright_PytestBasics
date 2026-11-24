#Concatenamos diferentes tipos de datos en este tipo un entero y un string
a=10
print("{} {}".format("Values is:", a))

#Los corchetes que se agragan deben ser
# iguales a la cantidad de valores que vamos a concatenar
# Concatenamos diferentes tipos de datos en este tipo un entero y dos string
b=10.9
print("{} {} {}".format("Values is:", b, ":)"))

#Concatenamos pero son los mismos tipo de datos
c="String 1"
d="String 2"
#Asi se imprime una misma cadena y definir variables{} seguir con el texto
print(f'La  concatenacion es {c+d} siguiente')

#Imprimimos el tipo de dato
print(type(a))
print(type(b))
print(type(c))


############################Excercise
age = 25
height = 5.10
favorite_color = "blue"

print("{} {}".format("Age:", age),"| Type:", type(age))
print("{} {}".format("Height:", height),"| Type:", type(height))
print("{} {}".format("Favorite_Color:", favorite_color),"| Type:", type(favorite_color))



