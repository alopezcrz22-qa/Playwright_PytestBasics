#Este archivo se centrara en guardar ycompartir fixtures,hooks,configuraciones globalmente
#el archivo por default lo nombraremos conftest.py
import pytest

#En este caso creamos un fixture nivel function, se ejecuta en cada una de las funciones en el que sea requerido
#ya sea que lo configuremos en dos clases diferentes o en las que sean necesarias al ser este nuestra configuracion
#global
#Ejemplo en el archivo PyTestBasic configuramos el fixture creado y en ptra clase Ejemploconftest de igual manera
@pytest.fixture(scope='function')
def preSetupWork():
    print('preSetupWork')

#YIELD
@pytest.fixture(scope='function')
def preSetupWorkYield():
    #Este codigo se ejecuta en todas las funciones que hagan uso del fixture y se imprime al inicio
    #pre-execution
    print('preSetupWork')
    #Actua como un interruptor o pausa en el fixture y cede ek control a la funcion que hagan uso del fixture
    yield
    #Deja de estar en pausa y se vuelve a ejecutar el fixture
    #post-execution
    print('Espero a que se ejecute la primer funcion test y despues me ejecuto yo')

@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param