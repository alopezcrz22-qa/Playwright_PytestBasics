str = " RahulShettyAcademy.com "
str1= "Consulting QA"
str2= "RahulShetty"

print(str[1]) #Imprime el valor del string en la psocion 1
print(str[0:5]) #Imprime el valor del string en la psocion 0 al 5

print(str+str1) #Concatena los datps

print(str2 in str) #Valida si en la cadena str2 existe coicidencia en la cadena str1

#Separa la cadena en dos "RahulShettyAcademy.com" hasta el valor "."
var =str.split('.')
print(var)

#Extrae la cadena primer posicion " RahulShettyAcademy" y guardalo en una variable
separate= var[0]
#Elimina el espacio al inicio del string
print(separate.strip())
#Elimina el espacio al final del string
print(separate.lstrip())
#Regresa el espacio al final del string
print(separate.rstrip())