from asyncio import timeout
from time import time

from playwright.sync_api import expect

from .checkoutPage import CheckoutPage

class CartPage:
    """Page Object Model (POM) para representar y gestionar las acciones
    en la página del carrito de compras.
    """
    def __init__(self, page):
        """Inicializa la clase CartPage.
        :param page: Instancia del navegador o página actual (ej. Playwright
        Page)
        """
        self.page = page

    def validateProductsVisible(self, listofMyProducts):
    # Define el localizador para obtener los títulos (h3) de los productos presentes en la lista del carrito
        cartPageProducts = self.page.locator('.cartWrap h3')
    # Itera sobre los productos deseados para confirmar su presencia en el carrito
        for cartProduct in listofMyProducts:
    # Filtra la lista de títulos por producto y verifica mediante una aserción que sea visible en la pantalla
            expect(cartPageProducts.filter(has_text=cartProduct)).to_be_visible()
            #return cartPageProducts.filter(has_text=cartProduct).to_be_visible()

    """Elimina un producto específico del carrito de compras.

            :param thisproductEliminate: Nombre o identificador del producto a
              eliminar.
            """
    def deleteProduct(self,thisproductEliminate):
    # Define el localizador para cada contenedor completo del ítem dentro del carrito
        cartCardProducts = self.page.locator('.infoWrap')

    # Filtra la tarjeta contenedora del producto que definamos en el test
    # y hace clic en su botón eliminar (clase '.btn-danger')
        cartCardProducts.filter(has_text=thisproductEliminate).locator('.btn-danger').click()

    def gotoCheckout(self):
    # Hace clic en el botón 'Checkout' para iniciar el proceso de pago
        self.page.get_by_role('button', name='Checkout').click()
    # Inicializa el Page Object Model (POM) de la página de pago usando la sesión actual
        checkoutPagePom = CheckoutPage(self.page)
        return checkoutPagePom


