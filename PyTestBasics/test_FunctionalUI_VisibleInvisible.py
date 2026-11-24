from playwright.sync_api import Page, expect


def test_UIFunctionalValidations(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractise/')
    #Valida que el elemento localizado por placeHolder es visible
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    #Da click en el boton Hide(desaparece el elemento)
    page.get_by_role('button', name='Hide').click()
    # Valida que el elemento localizado por placeHolder es invicible
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()
