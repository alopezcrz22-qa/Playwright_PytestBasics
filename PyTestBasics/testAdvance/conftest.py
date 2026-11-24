#Este archivo se centrara en guardar y compartir fixtures,hooks,configuraciones globalmente
#el archivo por default lo nombraremos conftest.py
from urllib import request

import pytest

# Hook de pytest para agregar un argumento personalizado a la línea de comandos
#Este hook proviene de la pagina oficial de pytest
def pytest_addoption(parser):
  parser.addoption(
      '--browser_name',
      action='store',
      default='chrome',
      help='Especifica el tipo de navegador (ej. chrome, firefox)',
  )
  parser.addoption(
      '--url_name',
      action='store',
      default='SIT',
      help='Especifica el ambiente en el que se esta ejecutando (ej. SIT, UAT, PERF)'
  )

# Fixture para manejar credenciales de usuario parametrizadas a nivel de sesión
#Uso en el arhcivo de JSON
@pytest.fixture(scope='session')
def user_credentials(request):
  return request.param


# Fixture para inicializar y gestionar el ciclo de vida y eleccion del navegador con Playwright
@pytest.fixture
def browserInstance(playwright, request):
  global browser
  # Obtiene  y define el valor del argumento '--browser_name' pasado desde la línea de comandos
  browser_name = request.config.getoption('browser_name')
  # Obtiene  y define el valor del argumento '--url_name' pasado desde la línea de comandos
  #url_name = request.config.getoption('url_name')

  # Inicia el navegador correspondiente en modo con interfaz gráfica (headless=False)
  if browser_name == 'chrome':
    browser = playwright.chromium.launch(headless=False)
  elif browser_name == 'firefox':
    browser = playwright.firefox.launch(headless=False)
  # Crea un nuevo contexto de navegador aislado
  context = browser.new_context()
  # Abre una nueva página/pestaña dentro del contexto
  page = context.new_page()

  # Indica la direccion del ambiente correspondiente
  #if url_name =='SIT':
  #  page.goto('https://www.sit.papel.com.mx')
  #elif url_name == 'UAT':
  #  page.goto('https://www.uat.papel.com.mx')
  #elif: url_name == 'PERF':
  #  page.goto('https://www.perf.papel.com.mx')

  # 'yield' entrega la página para que la prueba se ejecute
  yield page

  # Código de limpieza (teardown) que se ejecuta al terminar la prueba
  context.close()
  browser.close()