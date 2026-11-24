#Describe la funcionalidad
Feature: Online Shop
  # Como cliente de la tienda online
  # Quiero agregar productos al carrito
  # Para realizar compras de manera segura

#Precondiciones
  Background:
    Given the user is logged into the online store

#Caso de prueba individual
  Scenario Outline: The user complete an Successful purchase
  #Estado Inicial
    Given the user is on the dashboard page
  #Accion del usuario
    When user add <producto> in to the cart
    And Complete the order purchase
  #Resultadp esperado
    Then the order should be successfully created
    #And an order confirmation number should be generated

#Caso de prueba individual
  Scenario Outline:The user add product not available in inventory.
  #Estado Inicial
    Given the user is on the dashboard page
  #Accion del usuario
    When user add <producto> in to the cart
  #Resultadp esperado
    Then the order message "Out of stock" should be displayed

#Caso de prueba individual
  Scenario Outline: The user has a valid coupon and must apply a discount.
  #Estado Inicial
    Given the user add <producto> in to the cart
  #Accion del usuario
    When the user enter a <cupon> in to the Order page
  #Resultadp esperado
    Then should apply disccount in the order
    And the order should be successfully created

#Caso de prueba individual
  Scenario Outline: The user has a invalid coupon
  #Estado Inicial
    Given the user add <producto> in to the cart
  #Accion del usuario
    When the user enter a <cupon> in to the Order page
  #Resultadp esperado
    Then should'nt apply disccount in the order
    And the order should message "Invalid cupon" should be displayed

#Caso de prueba individual
  Scenario Outline: The user can add multiple products to the cart.
  #Accion del usuario
    Given the user is on the dashboard page
  #Resultadp esperado
    When the user add <items_products> in to the cart
    And Complete the order purchase
  #Resultadp esperado
    Then the order should be successfully created







