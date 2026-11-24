#Una función en Python es un bloque de código reutilizable
# que realiza una tarea específica y se ejecuta solo cuando es llamado

#De la siguiente manera definimos una funcion
#def funcionName(parametros que recibira):
def print_hi(name):
    # Acciones
    print(f'Hello, {name}')
#Fuera de la funcion mandamos a llamar la funcion y enviamos el parametro
print_hi('PyCharm')


#De la siguiente manera definimos una funcion
def GreetMe():
    # Acciones
    print("Good Morning")
#Mandamos a llamar la funcion
GreetMe()


#Definimos una funcion que recibira los parametros a y b
def AddIntegers(a, b):
    #Accion , return y imprime los siguiente
    return print(f'La suma es : {a+b}')
#Mandamos a llamar la funcion y enviamos los parametros
AddIntegers(1, 2)

#Tambien se puede crear una funcion si hacer la palabra clave "return"
# Definimos una funcion que recibira los parametros a y b
def RestIntegers(a, b):
    #Accion , return y imprime los siguiente
    print(f'La resta es : {a-b}')
#Mandamos a llamar la funcion y enviamos los parametros
RestIntegers(2, 1)

#O tambien se puede crear la imprimicion al mandar llamar la funcion
# Definimos una funcion que recibira los parametros a y b
def XIntegers(a, b):
    #Accion , return y imprime los siguiente
    return a*b
#Mandamos a llamar la funcion y enviamos los parametros
print(XIntegers(2, 1))


##################G#########Exercise
def GreetUser(name):
    print(f'Hello, {name}!, Welcome to the Pyhton Course')
GreetUser('PyCharm')