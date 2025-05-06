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
Interacts with alert page
    library.alert simple dialog
    library.alert confirm dialog
    library.Sweet Alert Dialog
    library.Sweet Model Dialog
    library.Alert Prompt Dialog
    library.Sweet Alert Confirmation Dialog
    library.Min And Max Dialog
