*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${PRODUCT_PAGE_HEADER}    css=div.product_label

*** Keywords ***
Click an Item By name
    [Arguments]    ${item_name}
    Click Element    xpath=//div[text()="${item_name}"]