#En Python, el constructor principal de una clase es el método especial
# __init__(), que se ejecuta de forma automática al crear una nueva instancia del objeto
# . Su función es inicializar los atributos de la clase.

#class Calculator:
    #Variables de tipo clase, porque pertence a la clase
    #num=100

    #Constructor por defecto: No recibe parámetros adicionales aparte de self
    # (o puede tener valores predeterminados asignados en los parámetros).
    #def __init__(self):
        #print('I am constuctor por defecto')

#obj = Calculator()

#################################################################
#No es obligatorio crear un constructor (__init__) para crear un objeto en Python.
#Si no lo escribes, Python genera automáticamente un constructor vacío por defecto
# en segundo plano para que puedas crear el objeto sin problemas.

# Creamos una clase -> ClassName
class CalculatorA:
    #Definimos una variable de tipo -> Clase
    num=100

    # Constructor parametrizado: Acepta argumentos externos para personalizar
    # los atributos de cada objeto al momento de crear.
    def __init__(self, a, b):
        #Definimos de tipo -> Instancia
        #y guarda el valor recibido (a) dentro del objeto actual(firstNumber)
        self.firstNumber=a
        # y guarda el valor recibido (b) dentro del objeto actual(secondNumer)
        self.secondNumber=b
        #Imprime un mensaje que confirma la ejecución del constructor.
        print('I am constructor parametrizado')

    # Define un método normal de la clase que no recibe parámetros extra.
    def getData(self):
        # Imprime un mensaje que confirma que el método se está ejecutando.
        print('I am metodo funcion por defecto')

    # Define un método para realizar una operación matemática.
    def add(self):
        # Suma los dos valores del objeto más la variable de clase (100)
        # y devuelve el resultado.
        # Lo hacemos haciendo uso de la plabra clave self para variables ->instancia
        # o mandando a llamar directamente la clase en variables -> clase
        return self.firstNumber+self.secondNumber+CalculatorA.num

#Crea el objeto 'obj' pasando los valores 10 y 20 al constructor.
obj = CalculatorA(10,20)
# Llama al método para imprimir el mensaje de confirmación en pantalla.
obj.getData()
# Llama al método de suma, calcula el total (10 + 20 + 100) e imprime el resultado (130).
print(obj.add())