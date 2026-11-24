from xml import parsers

import pytest
from playwright.sync_api import expect, Playwright

#Importamos los valores bdd
from pytest_bdd import given, when, then, scenarios, parsers

from pageObjectModel import loginPage
#Importamos la clase loginPagePom
#Las demas clases no porque ya lo hicimos en cada uno por medio de PageObjectModel
from pageObjectModel.loginPage import LoginPagePOM

#Importamos la ubicacion del archivo feature
scenarios('features/letsShop.feature')

#Este fixture va ser el encargado de compartir objetos y valores desde un metodo, un objeto a otro
#en este caso desde un given a un then, set(envia) y get(obtiene)
@pytest.fixture
def shared_objectData():
    return {}


# GIVEN:
# Define el estado inicial del escenario.
#Para definir el metodo , solo es necesario copiar tal cual como lo definimos en el feature
@given('The user is on the main login page')
#Definimos en nombre de nuestra funcion
#En este caso definimos el browserInstance de conftest y el fixture shared_objectData
def goTo_loginPage(browserInstance,shared_objectData):
    # Inicializa el objeto basado en el Page Object con la página de Playwright y abre el login
    loginPagePom = LoginPagePOM(browserInstance)
    loginPagePom.goto_login_page()
    # SET // Fixture shared_objectData
    shared_objectData['login_PagePom'] = loginPagePom

# WHEN:
#solo es necesario copiar tal cual como lo definimos en el feature
#En este caso como vamos a ingresar username y password lo enviamos como parametros pero ahora con {}{}
#parser.parse , solo es necesario cuando agregemos valores que recibiremos en este caso usernam,password
@when(parsers.parse('Add credentials {username} and {password}'))
#Definimos en nombre de nuestra funcion
#En este caso definimos el fixture shared_objectData y los parametros que recibiremos
def addCredentials(shared_objectData, username, password):

    # GET // object shared_objectData
    loginPagePom = shared_objectData['login_PagePom']

    #Al haber creado el objeto de dashboardPage  en la clase Login
    # Ejecuta el inicio de sesión con las credenciales del usuario y almacena el objeto de la página siguiente (DashboardPage)
    dashboardPagePom =loginPagePom.login(username, password)

    # SET // Fixture shared_objectData
    shared_objectData['dashboard_PagePom'] = dashboardPagePom


@then('LogIn successfully verify the visibility of a message on the dashboard')
def logInSuccess(playwright:Playwright, shared_objectData):

    # GET // object shared_objectData
    dashboardPagePom = shared_objectData['dashboard_PagePom']

    # DashboardPage
    # Guardamos en una variable , la funcion que en este caso nos retornara un locator
    textReturn = dashboardPagePom.validateText()

    # Agregamos el expect aqui, porque creo yo validaciones deberia ser aqui en el test
    # Valida mediante una aserción que el elemento con clase '.blink_me' contenga el texto exacto del mensaje
    expect(textReturn).to_have_text('User can only see maximum 9 products on a page')







@then('an order confirmation number should be generated')
def an_order_confirmation_number_should_be_generated():
    raise NotImplementedError
