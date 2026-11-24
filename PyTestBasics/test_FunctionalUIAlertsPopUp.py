import time

from playwright.sync_api import Page, expect


def test_UIFunctional(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractise/')

#Detectar y aceptar alertas
#El método page.on() permite registrar un controlador para escuchar eventos que ocurren en una página.
#El evento dialog se produce cuando la página abre un cuadro de diálogo nativo del navegador.
#Una función lambda permite crear una función pequeña de una sola expresión.
    page.on('dialog', lambda dialog: dialog.accept())

    #Esta línea realiza una acción sobre un elemento de la página web.
    page.get_by_role('button', name='Confirm').click()
    time.sleep(5)

