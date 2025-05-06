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

Verify which is your favourite UI Automation tools
    [Arguments]     ${select_tool_dropdown}

    library.Select By Label     ${select_tool_dropdown}
Verify Choose your preferred country
    [Arguments]     ${select_country}
    library.Country Dropdown    ${select_country}
Verify Choose the course
    [Arguments]     ${select_course}
    library.Course Dropdown    ${select_course}



