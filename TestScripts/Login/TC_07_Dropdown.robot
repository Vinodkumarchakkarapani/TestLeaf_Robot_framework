*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium

Library     ${EXECDIR}/Py/library.py
Resource       ../../Objects/Object.robot
#Resource     ../../Pageclass/Leaf_ground.robot
Resource     ../../Pageclass/Page_dropdown.robot

*** Test Cases ***

interacts with dropdown page
    open the browser
    Verify which is your favourite UI Automation tools      ${select_tool_dropdown}
    Verify Choose your preferred country    ${select_country}
    Verify Choose the course    ${select_course}
