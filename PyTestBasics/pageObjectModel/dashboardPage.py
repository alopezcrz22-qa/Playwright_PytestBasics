from .cartPage import CartPage


class DashboardPage:

    def __init__(self, page):
        self.page = page
        # Define el localizador base que selecciona todas las tarjetas de productos en el catálogo
        #Lo agrego aqui para demostrar que puedo definir una variable de instancia
        #solo seria necesario agregar self.cardProducts en la funcion
        #self.cardProducts = page.locator(".card")

    def validateText(self):
        # Valida mediante una aserción que el elemento con clase '.blink_me' contenga el texto exacto del mensaje
        return self.page.locator('.blink_me')

    def addItemsToCart(self, listofMyProducts):
        # Define el localizador base que selecciona todas las tarjetas de productos en el catálogo
        cardProducts = self.page.locator(".card")

        # Itera sobre cada uno de los productos definidos en la tupla
        for thisProduct in listofMyProducts:
            # Filtra las tarjetas por el nombre del producto actual y hace clic en su respectivo botón 'Add To Cart'
            cardProducts.filter(has_text=thisProduct).get_by_role('button', name=' Add To Cart').click()

    def goToCartPage(self):
        # Localiza la barra de navegación y hace clic en el botón para ir al carrito de compras
        self.page.get_by_role('navigation').get_by_role('button', name='  Cart ').click()

        # Instancia el Page Object de la página del carrito (CartPage) pasándole la misma sesión del navegador (self.page)
        cartPagePom = CartPage(self.page)

        # Retorna la nueva instancia para continuar ejecutando acciones y validaciones dentro del carrito
        return cartPagePom
