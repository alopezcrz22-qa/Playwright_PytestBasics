Feature: Lets Shop
    Como usuario de RahulShettyAcademy
    Debo agregar productos al carrito de compras
    Y realizar una compra exitosa

   Scenario Outline:the user has successfully logged into the platform
    Given The user is on the main login page
    When  Agregate credentials <username> and <password>
    Then LogIn successfully verify the visibility of a message on the dashboard

    Examples:
        | username             | password       | listofMyProducts                |
        | alanbarc614@gmail.com| .$vcMuTCM8G$pY!| ZARA COAT 3                     |
        | aalanlz210m@gmail.com| @reS1823       | ZARA COAT 3, ADIDAS ORIGINAL    |


