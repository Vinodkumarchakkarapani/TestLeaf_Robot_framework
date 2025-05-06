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

Interacts with draganddrop page
    library.Drag And Drop
    library.Drag Drop Target

