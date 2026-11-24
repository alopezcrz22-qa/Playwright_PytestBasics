#Uso sincronica es secuancial,son para scripts rapidos,pruebas estandar
from playwright.sync_api import Playwright, Page
#Uso asincronica es para aplicacione de alto rendimiento ,concurrencia masiva, FastApi
#from playwright.async_api import Playwright, Page


#############ContextBrowser################
#De la siguiente manera definimos un nuevo @test y enviamos el parametro playwright del objeto PLaywright
def test_playwrightBrowserContext(playwright:Playwright):
    #Creamos una variable browser que abrira(lanzara) el navegador
    #en este caso el metodo headless sera falso(Si abrira el navegador)
    browser = playwright.chromium.launch(headless=False)
    #Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    #Abrir una nueva page
    page = context.new_page()
    #Dirigir a la pagina referenciada
    page.goto("https://www.google.com")


###########PageBrowser################
# De la siguiente manera definimos un nuevo @test y enviamos el parametro page del parametro PAGE
def test_playwrightPageBrowser(page:Page):
    page.goto("https://www.google.com")