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
Interact with Window

    library.Page Single Window
    library.Page Multiple Window
    library.Except Main Window