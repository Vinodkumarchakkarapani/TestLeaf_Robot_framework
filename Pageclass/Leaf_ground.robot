*** Settings ***
#Library     AppiumLibrary
Library     SeleniumLibrary
Library     Selenium2Library
#Library     properties
#Library     Lib
Library     Collections

Library     ../Py/properties.py
Library    ../Py/library.py
#Library     ../Py/library.py

Resource    ../Py/library.py
Resource    ../Objects/Object.robot

*** Variables ***

*** Keywords ***
Open the browser
    [Arguments]
    library.open browser    ${url}
Interacting with textbox elements
    library.textbox element
    library.interact type your name
    library.retrieve text
    library.error message text

