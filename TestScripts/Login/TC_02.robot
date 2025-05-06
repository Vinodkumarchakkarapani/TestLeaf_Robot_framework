*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium

Library     ../../Py/library.py

#Resource     ../../Pageclass/Leaf_ground.robot
Resource     ../../Pageclass/Page_alert.robot

*** Test Cases ***

TC_01 interacting with alert page
    open the browser
    interacts with alert page
