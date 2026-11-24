#Creamos la clase LoginPagePOM, la cual contendra funciones,atributos de la clase Login
from pytest_playwright.pytest_playwright import page
#Importamos la clase dashboard Page, en este caso al pertenecer a la misma carpeta raiz asi se importa
# '.'
from pageObjectModel.dashboardPage import DashboardPage


class LoginPagePOM:
    #Definimos un contructor parametrizado, el cual al pertenecer a la clase recibe su parametro self
    #ademas de el parametro page, que en este caso es el page.(goto,locator)
    def __init__(self, page):
        #Definimos que this.page=page
        self.page = page


    #Ahora definimos una funcion que al abrir login page, nos dirigira a la pagina principal siempre
    def goto_login_page(self):
        self.page.goto('https://rahulshettyacademy.com/client/#/auth/login')

    #Definimos una funcion que nos permitira logearnos, siempre para mandar a llamar page,necesitamos self
    #ademas que al enviar valores que no pertenecen o almacenamos en esta clase, entonces recibiremos
    #parametros user_email, user_password
    def login(self, user_email, user_password):
        # Localiza el campo de correo por su ID '#userEmail' e ingresa el email correspondiente
        # al ser datos externos solo agregamos como lo definimos en la funcion user_email
        self.page.locator('#userEmail').fill(user_email)
        # Localiza el campo de contraseña por su ID '#userPassword' e ingresa la contraseña
        # al ser datos externos solo agregamos como lo definimos en la funcion user_password
        self.page.locator('#userPassword').fill(user_password)
        # Busca el botón de inicio de sesión usando el atributo CSS selector `input[id='login']` y le da clic
        self.page.locator("input[id='login']").click()

        # Instancia el Page Object de la página de destino (DashboardPage) pasándole la sesión actual del navegador (self.page)
        dashboardPagePom = DashboardPage(self.page)

        # Retorna la nueva instancia para encadenar acciones directamente en la siguiente página tras iniciar sesión
        return dashboardPagePom
