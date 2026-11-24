import pytest

                                        #scope="module"
#Define una fixture con alcance de módulo (se ejecuta una sola vez antes de todos los tests del archivo)
#En este ejemplo se imprimira solo en la funcion test_miPrimerTest()
@pytest.fixture(scope="module")
def preWork():
    print('preWork')

# Primer caso de prueba; recibe la fixture 'preWork' como dependencia
def test_miPrimerTest(preWork):
    print('miPrimerTest')

# Segundo caso de prueba; también reutiliza la fixture 'preWork'
def test_miSecondTest(preWork):
    print('miSecondTest')



                                 #scope="function"
#Indica que la fixture se ejecutará una vez por cada función de prueba que la solicite
#(se ejecuta antes de cada test y se limpia al terminar).
#En este ejemplo se imprimira en las dos funciones test_miPrimerTest()/test_miSegundoTest()
@pytest.fixture(scope="function")
def preWorkFunction():
    print('preWork')

# Primer caso de prueba; recibe la fixture 'preWork' como dependencia
# Recibe dos fixture uno creado en esta clase y otro agregado en el archivo conftest
def test_miPrimerTestF(preWorkFunction,preSetupWork):
    print('miPrimerTest')

# Segundo caso de prueba; también reutiliza la fixture 'preWork'
def test_miSecondTestF(preWorkFunction):
    print('miSecondTest')



                                        #scope="session"
#indica que la fixture se ejecuta una sola vez para toda la sesión de pruebas
# (es decir, abarca todos los archivos y funciones de test que ejecutes en esa misma ejecución de pytest).
#En este caso asi tengamos 40 archivos o clases solo se ejecutara una sola vez por las 40
@pytest.fixture(scope="session")
def preWorkSession():
    print('preWork')

# Primer caso de prueba; recibe la fixture 'preWork' como dependencia
def test_miPrimerTestS(preWorkSession):
    print('miPrimerTest')

# Segundo caso de prueba; también reutiliza la fixture 'preWork'
def test_miSecondTests(preWorkSession):
    print('miSecondTest')


                                #scope="class"
#indica que la fixture se ejecuta una sola vez en cada una de las sesiónes de pruebas
# (es decir, abarca todos los archivos y funciones de test que ejecutes en esa misma ejecución de pytest).
#En este caso asi tengamos 40 archivos o clases si se ejecutara una sola vez en las 40
@pytest.fixture(scope="class")
def preWorkClass():
    print('preWork')

# Primer caso de prueba; recibe la fixture 'preWork' como dependencia
def test_miPrimerTestC(preWorkClass):
    print('miPrimerTest')

# Segundo caso de prueba; también reutiliza la fixture 'preWork'
def test_miSecondTestC(preWorkClass):
    print('miSecondTest')
