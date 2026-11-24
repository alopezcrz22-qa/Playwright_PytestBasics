from playwright.sync_api import Page


def test_handleChildWindowsFunc(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')

    # Usamos un administrador de contexto (with) para esperar y capturar
    # la nueva pestaña (popup) que se abrirá al hacer clic en el enlace
    with page.expect_popup() as newPage_info:
        # Step 1: Hacemos clic en el enlace que abre la nueva ventana/pestaña
        page.get_by_role('link', name='Free Access to InterviewQues/ResumeAssistance/Material').click()

        # Obtenemos la instancia de la nueva página (child page) una vez que se abre
        childPage = newPage_info.value

        # Localizamos el elemento con la clase '.red' en la nueva pestaña
        # y extraemos su contenido de texto
        text = childPage.locator('.red').text_content()

        # Imprimimos el texto extraído en la consola
        print(text)#Please email us at mentor@rahulshettyacademy.com with below template to receive response
