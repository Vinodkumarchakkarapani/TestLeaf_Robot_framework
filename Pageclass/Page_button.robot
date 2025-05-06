*** Settings ***
Library     ../Py/properties.py
Library     ../Py/library.py


Resource    ../Py/library.py
Resource    ../Objects/Object.robot

*** Variables ***

*** Keywords ***
Open the browser
    [Arguments]
    library.open browser    ${url}

Verify click and confirm title in Leafground page
    library.Clickandconfirm Title
Verify confirm if the button is disabled
    library.Confirm Button Disabled
Verify find the position of the submit button
    library.Button Position
Verify find the height and width of this button
    library.Find H W Button
Verify mouse over and confirm the color changed
    library.Button Hover Color Change
Verify how many rounded buttons are there?
    library.Count Round Button
