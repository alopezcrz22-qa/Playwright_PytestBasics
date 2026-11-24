from wsgiref import validate

from pageObjectModel.confirmationPage import ConfirmationPage


class CheckoutPage:
    def __init__(self, page):
        self.page = page
    def validateText(self):
        # Valida mediante una aserción que el encabezado/texto 'Payment Method' sea visible en la pantalla
        validateTextPage= self.page.get_by_text(' Payment Method ')
        return validateTextPage

    def completeOrder(self,countryOrder):
        # Define el localizador para el campo de texto con el placeholder 'Select Country'
        countryPlaceHolder = self.page.get_by_placeholder('Select Country')

        # Escribe la cadena 'Me' letra por letra en el input con una pausa de 150 milisegundos entre cada carácter
        countryPlaceHolder.press_sequentially(countryOrder, delay=150)

        # Busca el menú desplegable de resultados (.ta-results), filtra la opción 'Mexico' y le da clic
        self.page.locator('.ta-results').locator("button[type='button']").filter(has_text=' Mexico').click()

    def gotoConfirmationPage(self):
        # Localiza la etiqueta enlace `<a>` dentro del div con clase 'actions' y hace clic para finalizar la compra
        self.page.locator("div[class='actions'] a").click()
        confirmationPagePom = ConfirmationPage(self.page)
        return confirmationPagePom