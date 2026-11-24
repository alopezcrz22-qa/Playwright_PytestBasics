#La herencia en Python es un mecanismo de la programación orientada a objetos (POO)
# que permite crear una nueva clase (llamada clase hija o subclase) a partir de una
# existente
# (llamada clase padre o superclase), heredando sus atributos y métodos

#Clase hija importada
from PythonBasics.BasicCalculator import BasicCalculator

#Creamos una nueva clase y dentro del parentesis agregamos el nombre de la clase hija
#importamos la clase
class ChildClass(BasicCalculator):  # Define una clase hija que hereda de BasicCalculator
    num2 = 100                      # Define una variable de clase hija con el valor 100

    def __init__(self):             # Constructor de la clase
        BasicCalculator.__init__(self, 2, 5)  # Llama al constructor de la clase padre
                                                    # pasándole los valores self y valores a y b
                                                    #de la clase hija

    def getCompleteData(self):      # Define un método para obtener datos completos
        return f'Complete Data: {self.num2} + {self.c} '  # Retorna un texto con num2 y la variable 'c' del padre

obj = ChildClass()                  # Crea una instancia (objeto) de ChildClass
print(obj.getCompleteData())        # Imprime en consola el resultado de ejecutar el método
