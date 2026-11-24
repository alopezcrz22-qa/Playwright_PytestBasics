from playwright.sync_api import Page, expect
#Mouse Hove: Pasar sobre un elemento tipo menu de amazon y dar click a una opcion

def test_UIFunctionalMouseHover(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractise/')
    #Mediante el localizador css(id), pasamos sobre el elemento(hover)
    page.locator('#mousehover').hover()
    #Una vez estando sobre el elemento y abrir las opciones ,damos click al link
    page.get_by_role('link', name='Top').click()
