import time

from playwright.sync_api import Playwright, expect

#define un test en donde recibiras parametro playwright
def test_firefox(playwright:Playwright):
    # Lanza el navegador Firefox en modo visible (no oculto)
    firefoxBrowser = playwright.firefox.launch(headless=False)

    # Abre una nueva pestaña o página en el navegador creado
    page = firefoxBrowser.new_page()

    # Navega a la página de prácticas de inicio de sesión
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')

    # Busca el campo por su etiqueta de texto y escribe el usuario
    page.get_by_label('Username:').fill('rahulshettyacademy')

    # Busca el campo por su etiqueta de texto y escribe la contraseña
    page.get_by_label('Password:').fill('learning')

    # Selecciona la opción 'Consultant' en el menú desplegable (combobox)
    page.get_by_role('combobox').select_option('Consultant')

    # Selecciona la casilla de verificación de términos usando su ID de CSS
    page.locator('#terms').click()

    # Hace clic en el enlace que contiene el texto de términos y condiciones
    page.get_by_role('link', name='terms and conditions').click()

    # Hace clic en el botón con el texto 'Sign In' para iniciar sesión
    page.get_by_role('button', name='Sign In').click()

    # Valida con un assert si la clase o el mensaje contiene to_contain_text o to_have_text
    expect(page.locator('.alert-danger')).to_contain_text('Old password "learning" is no longer valid.')

