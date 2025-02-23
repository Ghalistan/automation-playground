*** Settings ***
Resource            ../resources/login.resource
Resource            ../resources/home.resource
Resource        ../resources/item_detail.resource
Resource        ../resources/header_component.resource
Resource        ../resources/cart.resource
Resource        ../resources/overview.resource
Library           SeleniumLibrary

*** Variables ***
${CHROME_DRIVER_PATH}    /drivers/chromedriver

*** Test Cases ***
Buy a product
    Open Browser    https://www.saucedemo.com/v1/    chrome
    Login to Application    standard_user    secret_sauce
    Wait Until Element Is Visible    ${PRODUCT_PAGE_HEADER}

    Click an Item By name    Sauce Labs Backpack
    Click Button    ${ADD_TO_CART_BUTTON}
    Click Element    ${CART_BUTTON}
    Click Element    ${CHECKOUT_BUTTON}

    Input Payment Details    John    Doe    12345
    Click Element    ${OVERVIEW_FINISH_BUTTON}
    Wait Until Element Is Visible    xpath=//h2[text()="THANK YOU FOR YOUR ORDER"]