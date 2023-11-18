*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py


*** Keywords ***
Login Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Login Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login