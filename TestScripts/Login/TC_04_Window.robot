*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium

Library     ${EXECDIR}/Py/library.py

#Resource     ../../Pageclass/Leaf_ground.robot
Resource     ../../Pageclass/Page_window.robot

*** Test Cases ***

TC_01 interacting with windows page
    open the browser
    Interact with Window
