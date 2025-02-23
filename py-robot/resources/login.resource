*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${USER_NAME}    css=input#user-name
${PASSWORD}     css=input#password
${LOGIN_BUTTON}     css=input#login-button

*** Keywords ***
Login to Application
    [Arguments]    ${name}    ${pass}
    Input Text    ${USER_NAME}    ${name}
    Input Text    ${PASSWORD}    ${pass}
    Click Element    ${LOGIN_BUTTON}