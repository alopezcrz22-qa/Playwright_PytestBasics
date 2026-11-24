import time

from playwright.sync_api import Page, expect


def test_shopCart(page:Page):
    # Navega a la página de prácticas de inicio de sesión
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')

    # Busca el campo por su etiqueta de texto y escribe el usuario
    page.get_by_label('Username:').fill('rahulshettyacademy')

    # Busca el campo por su etiqueta de texto y escribe la contraseña
    page.get_by_label('Password:').fill('Learning@830$3mK2')

    # Selecciona la opción 'Consultant' en el menú desplegable (combobox)
    page.get_by_role('combobox').select_option('Consultant')

    # Selecciona la casilla de verificación de términos usando su ID de CSS
    page.locator('#terms').click()

    # Hace clic en el enlace que contiene el texto de términos y condiciones
    page.get_by_role('link', name='terms and conditions').click()

    # Hace clic en el botón con el texto 'Sign In' para iniciar sesión
    page.get_by_role('button', name='Sign In').click()

    # Creamos una [lista] de los productos agregar también puede ser una (tupla)
    productos = ("iphone X", "Samsung Note 8", "Nokia Edge", "Blackberry")

    # Captura la colección de todos los elementos (tarjetas de productos) que coinciden con la clase CSS '.col-md-6'
    #La card products se agrega de este lado aqui solo estamos definiendo el localizador
    #mismo que entrara al ciclo for
    cardProducts = page.locator('.col-md-6')

    # Filtra las tarjetas para identificar únicamente la que contiene el texto 'Samsung Note 8'
    # Luego localiza el botón con el texto 'Add ' dentro de esa tarjeta específica y hace clic en él
    #cardProducts.filter(has_text='Samsung Note 8').get_by_role('button', name='Add ').click()

    #Mediante cliclo for
    # Recorremos cada elemento (producto) dentro de la lista de productos
    for product in productos:
        #Estos elementos son agregados aqui ya que por cada iteraccion debe encontrar en la card el boton
        # Filtramos los elementos que contengan el texto del producto actual,
        # buscamos el botón cuyo nombre accesible comience o sea 'Add ' y hacemos clic en él
        cardProducts.filter(has_text=product).get_by_role(
            'button', name='Add '
        ).click()

    #Da click al boton checkout
    page.get_by_text('Checkout').click()

    #Valida que la card contenga 4 elementos, en este caso los productos
    expect(page.locator('.media-body')).to_have_count(5)

    time.sleep(5)