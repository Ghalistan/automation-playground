*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CHECKOUT_BUTTON}    css=a.checkout_button
${PAYMENT_FIRST_NAME}    css=input#first-name
${PAYMENT_LAST_NAME}    css=input#last-name
${PAYMENT_POSTAL_CODE}    css=input#postal-code
${PAYMENT_CONTINUE_BUTTON}    css=input[value="CONTINUE"]

*** Keywords ***
Input Payment Details
    [Arguments]    ${first_name}    ${last_name}    ${postal_code}
    Input Text    ${PAYMENT_FIRST_NAME}    ${first_name}
    Input Text    ${PAYMENT_LAST_NAME}    ${last_name}
    Input Text    ${PAYMENT_POSTAL_CODE}    ${postal_code}
    Click Button    ${PAYMENT_CONTINUE_BUTTON}
