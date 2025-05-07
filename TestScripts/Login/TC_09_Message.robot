*** Settings ***
Library     AppiumLibrary
#Library     SeleniumLibrary
#Library     Selenium2Library
#Library     selenium

Library     ../Py/library.py
Resource       ../../Objects/Object.robot
Resource     ../../Pageclass/Page_Message.robot

*** Test Cases ***

interacts with menu page
    open the browser
    Verify the messages info warn and Error
