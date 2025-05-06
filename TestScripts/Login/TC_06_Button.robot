*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium

Library     ${EXECDIR}/Py/library.py

#Resource     ../../Pageclass/Leaf_ground.robot
Resource     ../../Pageclass/Page_button.robot

*** Test Cases ***

TC_01 interacting with button page
    open the browser
    Verify click and confirm title in Leafground page
    Verify confirm if the button is disabled
    Verify find the position of the submit button
    Verify find the height and width of this button
    Verify mouse over and confirm the color changed
    Verify how many rounded buttons are there?
