import time

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.tagName #Declaramos una tagName que en linea de comando podemos ejecutar por su @tag
def test_LetsShopPython(page:Page):
    # Navega hacia la URL especificada de la página de inicio de sesión
    page.goto('https://rahulshettyacademy.com/client/#/auth/login')

    # Localiza el campo de correo por su ID '#userEmail' e ingresa el email correspondiente
    page.locator('#userEmail').fill('aalanlz210m@gmail.com')

    # Localiza el campo de contraseña por su ID '#userPassword' e ingresa la contraseña
    page.locator('#userPassword').fill('@reS1823')

    # Busca el botón de inicio de sesión usando el atributo CSS selector `input[id='login']` y le da clic
    page.locator("input[id='login']").click()

    # Valida mediante una aserción que el elemento con clase '.blink_me' contenga el texto exacto del mensaje
    expect(page.locator('.blink_me')).to_have_text('User can only see maximum 9 products on a page')

    # Línea comentada/desactivada: Validación alternativa que buscaba el texto directamente usando `get_by_text`
    # expect(page.get_by_text(' User can only see maximum 9 products on a page')).to_have_text(' User can only see maximum 9 products on a page')

    # Define una tupla de Python con los nombres de los productos que se van a agregar al carrito
    iwantThisProducts = ('ADIDAS ORIGINAL', 'ZARA COAT 3', 'iphone 13 pro')

    # Define el localizador base que selecciona todas las tarjetas de productos en el catálogo
    cardProducts = page.locator(".card")

    # Itera sobre cada uno de los productos definidos en la tupla
    for thisProduct in iwantThisProducts:
        # Filtra las tarjetas por el nombre del producto actual y hace clic en su respectivo botón 'Add To Cart'
        cardProducts.filter(has_text=thisProduct).get_by_role('button', name=' Add To Cart').click()

    # Localiza la barra de navegación y hace clic en el botón para ir al carrito de compras
    page.get_by_role('navigation').get_by_role('button', name='  Cart ').click()

    # --- SECCIÓN: CartPage (Página del Carrito) ---

    # Define el localizador para obtener los títulos (h3) de los productos presentes en la lista del carrito
    cartPageProducts = page.locator('.cartWrap h3')

    # Itera sobre los productos deseados para confirmar su presencia en el carrito
    for cartProduct in iwantThisProducts:
        # Filtra la lista de títulos por producto y verifica mediante una aserción que sea visible en la pantalla
        expect(cartPageProducts.filter(has_text=cartProduct)).to_be_visible()

    # Define el localizador para cada contenedor completo del ítem dentro del carrito
    cartCardProducts = page.locator('.cartWrap')

    # Filtra la tarjeta contenedora de 'iphone 13 pro' y hace clic en su botón eliminar (clase '.btn-danger')
    cartCardProducts.filter(has_text='iphone 13 pro').locator('.btn-danger').click()

    # Hace clic en el botón 'Checkout' para iniciar el proceso de pago
    page.get_by_role('button', name='Checkout').click()

    # --- SECCIÓN: CheckoutPage (Página de Pago) ---

    # Valida mediante una aserción que el encabezado/texto 'Payment Method' sea visible en la pantalla
    expect(page.get_by_text(' Payment Method ')).to_be_visible()

    # Define el localizador para el campo de texto con el placeholder 'Select Country'
    countryPlaceHolder = page.get_by_placeholder('Select Country')

    # Escribe la cadena 'Me' letra por letra en el input con una pausa de 150 milisegundos entre cada carácter
    countryPlaceHolder.press_sequentially('Me', delay=150)

    # Busca el menú desplegable de resultados (.ta-results), filtra la opción 'Mexico' y le da clic
    page.locator('.ta-results').locator("button[type='button']").filter(has_text=' Mexico').click()

    # --- SECCIÓN: ConfirmPage (Página de Confirmación) ---

    # Localiza la etiqueta enlace `<a>` dentro del div con clase 'actions' y hace clic para finalizar la compra
    page.locator("div[class='actions'] a").click()

    # Valida mediante una aserción que el encabezado del mensaje de confirmación coincida exactamente con el texto
    expect(page.locator("h1[class='hero-primary']")).to_have_text(' Thankyou for the order. ')

    # Pausa la ejecución del script por 5 segundos antes de continuar o finalizar
    time.sleep(5)
