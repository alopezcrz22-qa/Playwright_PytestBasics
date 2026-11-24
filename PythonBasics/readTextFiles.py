#1.- Leer el contenido del texto sencillo , solo estrayendo una linea de texto
#En una variable llamad file guardamos el valor de open('ubicacion/nombredelarchivo')
file= open('mytext.txt')
#Ahora imprimimos dicho archivo con la variable.read
print(file.read(2)) #El valor pertence a la cantidad de letras que quiero que se muestren pero de la primer linea
#siempre debemos cerrar dicho archivo de lo contratrio generaria error
file.close()


#2.- Leer el contenido del texto sencillo , solo estrayendo una linea de texto
#En una variable llamad file guardamos el valor de open('ubicacion/nombredelarchivo')
file= open('mytext.txt')
#Ahora imprimimos la primer linea del txt
print(file.readline())
#Ahora imprimimos la segunda linea del txt
print(file.readline())
#siempre debemos cerrar dicho archivo de lo contratrio generaria error
file.close()


#3.- Leer el contenido del texto avanzado
#Abre el txt en la ubicacion  en modo read(r) como un archivo
with open('mytext.txt', 'r', encoding='utf-8') as file:
    #Lee todo el contenido del txt
    content= file.read()
    #Imprime el contenido
    print(content)