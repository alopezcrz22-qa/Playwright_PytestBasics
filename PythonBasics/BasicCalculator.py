class BasicCalculator:
    c = 2
    def __init__(self,a, b):
        self.numbera = a
        self.numberb = b

    def add(self):
        return print(f'Addition: {self.numbera} + {self.numberb} + {BasicCalculator.c} ='
                     f'  {self.numbera + self.numberb + BasicCalculator.c}')
    def sub(self):
        return print(f'Substraccion: {self.numbera} - {self.numberb} - {BasicCalculator.c} ='
                     f'  {self.numbera - self.numberb - BasicCalculator.c}')
    def multi(self):
        return print(f'Multiplication: {self.numbera} * {self.numberb} * {BasicCalculator.c} ='
                     f'  {self.numbera * self.numberb * BasicCalculator.c}')
    def divide(self):
        return print(f'Division: {self.numbera} / {self.numberb} / {BasicCalculator.c} ='
                     f'  {self.numbera / self.numberb / BasicCalculator.c}')

obj = BasicCalculator(10,5)
obj.add()
obj.sub()
obj.multi()
obj.divide()


####################################################33
print('##############################')
class BasicCalculatorB:  # Define la clase llamada BasicCalculator.
    c = 2  # Atributo de clase (variable global para todos los objetos, vale 2).

    def __init__(self, a, b):  # Constructor que se ejecuta al crear el objeto; recibe dos valores.
        self.numbera = a  # Guarda el primer valor en el atributo de instancia 'numbera'.
        self.numberb = b  # Guarda el segundo valor en el atributo de instancia 'numberb'.

    # regresa el valor de la suma entre los valores de instancia y valor de la clase
    # de la siguiente manera se puede agragar varias lineas de codigo
    def add(self):  # Método para sumar.
        return print(
            f"Addition: {self.numbera} + {self.numberb} + {BasicCalculatorB.c} ="  # Imprime la operación de suma en pantalla.
            f"  {self.numbera + self.numberb + BasicCalculatorB.c}"
        )

    # regresa el valor de la resta entre los valores de instancia y valor de la clase
    # de la siguiente manera se puede agragar varias lineas de codigo
    def sub(self):  # Método para restar.
        return print(
            f"Substraccion: {self.numbera} - {self.numberb} - {BasicCalculatorB.c} ="  # Imprime la operación de resta en pantalla.
            f"  {self.numbera - self.numberb - BasicCalculatorB.c}"
        )

    # regresa el valor de la multiplicacion entre los valores de instancia y valor de la clase
    # de la siguiente manera se puede agragar varias lineas de codigo
    def multi(self):  # Método para multiplicar.
        return print(
            f"Multiplication: {self.numbera} * {self.numberb} * {BasicCalculatorB.c} ="  # Imprime la operación de multiplicación en pantalla.
            f"  {self.numbera * self.numberb * BasicCalculatorB.c}"
        )

    # regresa el valor de la divicion entre los valores de instancia y valor de la clase
    # de la siguiente manera se puede agragar varias lineas de codigo
    def divide(self):  # Método para dividir.
        return print(
            f"Division: {self.numbera} / {self.numberb} / {BasicCalculatorB.c} ="  # Imprime la operación de división en pantalla.
            f"  {self.numbera / self.numberb / BasicCalculatorB.c}"
        )


objB = BasicCalculatorB(10, 5)  # Crea el objeto 'obj' pasando 10 para 'a' y 5 para 'b'.
objB.add()  # Llama al método de suma (Resultado: 10 + 5 + 2 = 17).
objB.sub()  # Llama al método de resta (Resultado: 10 - 5 - 2 = 3).
objB.multi()  # Llama al método de multiplicación (Resultado: 10 * 5 * 2 = 100).
objB.divide()  # Llama al método de división (Resultado: 10 / 5 / 2 = 1.0).