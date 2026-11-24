# Recibe el fixture creado en el archivo conftest
#Al usar el fixture yield
# entonces se ejcuta primero lo que contenga el fixture y despues viene aqui y ejecuta la funcion
#despues regresa al fixture yield y ejecuta la ultima accion
import pytest

#funcion que recibe parametroa del archivo conftest
def test_thirdTest(preSetupWork,preSetupWorkYield):
    print('test_thirdTest')

#Significa que dicha funcion o test va ser saltado y no se ejecutara al momento de ejecutarlo
@pytest.mark.skip
def fourthTest():
    print('fourthTest')


#Significa que dicha funcion o test va ser tageado o pertence a la categoria @pytest.mark.tagName
@pytest.mark.smoketest
def fifthTest():
    print('fifthTest')