import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect
from PyTestBasics.pageObjectModel.loginPage import LoginPagePOM

# Construye la ruta absoluta hacia el archivo 'credentials.json', subiendo dos niveles desde el archivo actual y entrando a la carpeta 'data'
credentials_path = Path(__file__).resolve().parent.parent / 'data' / 'credentials.json'
# Abre el archivo JSON en modo lectura con codificación UTF-8 y carga su contenido como un diccionario de Python
with credentials_path.open(encoding='utf-8') as f:
    test_data = json.load(f)
# Extrae la lista de credenciales de usuario desde el diccionario cargado
user_credentials_list = test_data['user_credentials']

# Parametriza la prueba para que Pytest la ejecute una vez por cada juego de credenciales en la lista
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_LetsShopUsingJSON(playwright: Playwright, user_credentials, request):

    # Creamos una variable browser que abrira(lanzara) el navegador
    browser = playwright.chromium.launch(headless=False)
    request.addfinalizer(browser.close)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    request.addfinalizer(context.close)
    # Abrir una nueva page
    page = context.new_page()

    # Inicializa el objeto basado en el Page Object con la página de Playwright y abre el login
    loginPagePom = LoginPagePOM(page)
    loginPagePom.goto_login_page()

    # Extraemos del archivo JSON el campo de correo por su ID '#userEmail'
    user_email= user_credentials['userEmail']
    # Localiza el campo de contraseña por su ID '#userPassword'
    user_password = user_credentials['userPassword']

    # Completa el formulario enviando los parametros requeridos en la funcion login
    # e inicia sesión mediante el Page Object

    #Al haber creado el objeto de dashboardPage  en la clase Login
    # Ejecuta el inicio de sesión con las credenciales del usuario y almacena el objeto de la página siguiente (DashboardPage)
    dashboardPagePom =loginPagePom.login(user_email, user_password)

    #DashboardPage
    #Guardamos en una variable , la funcion que en este caso nos retornara un locator
    textReturn = dashboardPagePom.validateText()

    #Agregamos el expect aqui, porque creo yo validaciones deberia ser aqui en el test
    # Valida mediante una aserción que el elemento con clase '.blink_me' contenga el texto exacto del mensaje
    expect(textReturn).to_have_text('User can only see maximum 9 products on a page')

    # Define una tupla de Python con los nombres de los productos que se van a agregar al carrito
    #iwantThisProducts = ('ADIDAS ORIGINAL', 'ZARA COAT 3', 'iphone 13 pro')
    # Extraemos del archivo JSON la lista de los productos
    listofMyProducts= user_credentials['iwantThisProducts']

    #Funcion agregar os productos a mi carrito, que enviara el parametro listofMyProducts
    dashboardPagePom.addItemsToCart(listofMyProducts)

    # Localiza la barra de navegación y hace clic en el botón para ir al carrito de compras
    # Navega desde el panel principal hacia la página del carrito y guarda la instancia del nuevo Page Object (CartPage)
    #A que pagina me dirigo y de que pagina vengo
    cartPagePom = dashboardPagePom.goToCartPage()


    # --- SECCIÓN: CartPage (Página del Carrito) ---

    # Define el localizador para obtener los títulos (h3) de los productos presentes en la lista del carrito
    # Itera sobre los productos deseados para confirmar su presencia en el carrito
    cartPagePom.validateProductsVisible(listofMyProducts)

    # Define el localizador para cada contenedor completo del ítem dentro del carrito
    # Filtra la tarjeta contenedora de 'iphone 13 pro' y hace clic en su botón eliminar (clase '.btn-danger')
    #thisproductEliminate = 'ZARA COAT 3'
    cartPagePom.deleteProduct('ZARA COAT 3')

    # Hace clic en el botón 'Checkout' para iniciar el proceso de pago
    checkoutPagePom = cartPagePom.gotoCheckout()

    # --- SECCIÓN: CheckoutPage (Página de Pago) ---

    # Valida mediante una aserción que el encabezado/texto 'Payment Method' sea visible en la pantalla
    validateTextPage = checkoutPagePom.validateText()
    expect(validateTextPage).to_be_visible()

    # Define el localizador para el campo de texto con el placeholder 'Select Country'
    # Escribe la cadena 'Me' letra por letra en el input con una pausa de 150 milisegundos entre cada carácter
    checkoutPagePom.completeOrder('Me')
    # Busca el menú desplegable de resultados (.ta-results), filtra la opción 'Mexico' y le da clic

    # Localiza la etiqueta enlace `<a>` dentro del div con clase 'actions' y hace clic para finalizar la compra
    confirmationPagePom= checkoutPagePom.gotoConfirmationPage()

    # --- SECCIÓN: ConfirmPage (Página de Confirmación) ---
    # Valida mediante una aserción que el encabezado del mensaje de confirmación coincida exactamente con el texto
    messageConfirm= confirmationPagePom.confirmPage()
    expect(messageConfirm).to_have_text(' Thankyou for the order. ')

    # Pausa la ejecución del script por 5 segundos antes de continuar o finalizar
    time.sleep(5)
