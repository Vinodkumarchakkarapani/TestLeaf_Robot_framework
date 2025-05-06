*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium

Library     ../../Py/library.py

Resource     ../../Pageclass/Leaf_ground.robot

*** Test Cases ***

TC_01_user interacting leafground

    Open the browser
    Interacting with textbox elements


