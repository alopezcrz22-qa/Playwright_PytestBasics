#En Python, una clase es un molde o plantilla que define
# las propiedades (atributos) y los comportamientos (métodos)
# que tendrán los objetos creados a partir de ella

#Declaramos una clase class className:
class A:
    #En la clase definimos una (variable)
    number = 1
    message='Congratulations!'

    #Definimos una funcion dentro de la clase
    #Funciones independientes (fuera de una clase): No llevan self.
    #Se definen simplemente con la palabra clave def seguida del nombre de la función
    # y los parámetros que necesites (o ninguno).

    #Métodos dentro de una clase: Solo los métodos de instancia llevan self
    # como su primer parámetro obligatorio para hacer referencia al objeto actual.
    # y los parámetros que necesites adicionales (o ninguno).
    def say_hi(self,user):
        #Acciones en este caso para poder llamar una propiedad de la clase
        #o fuera de la funcion(metodo)
        #Lo hacemos haciendo uso de la plabra clave self o mandando a llamar directamente
        #el nombre de la clase
        print(f'Hello, {user} your ticket is {A.number} {A.message}!')
        #print(f'Hello, {user} your ticket is {self.number} {self.message}!')


#Creamos un objeto
#En java se llama de la siguiente manera
#className objectName = new className

#En python solo es necesario crear la objectName y llamar la className
obj = A()
#Ahora de ese objeto , podemos mandar a llamr la funcion(metodo) de la clase
#Y en este caso enviar el parametro requerido
obj.say_hi('Alan')
#podemos igual a mandar a llamar las propiedades creadas al principio
print(obj.number)

#Podemos crear n veces un nuevo objeto, con diferentes nombres
obj1 = A()
obj1.say_hi('Lorena')

