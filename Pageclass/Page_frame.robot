*** Settings ***
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
Interact with Frame

    library.Page Frame