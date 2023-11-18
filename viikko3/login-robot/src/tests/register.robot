*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  newuser
    Set Password  strongPassword123
    Confirm Password  strongPassword123
    Submit Registration
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  strongPassword123
    Confirm Password  strongPassword123
    Submit Registration
    Registration Should Fail With Message  Username has to be 3-20 characters and have only lowercase letters

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  t
    Confirm Password  t
    Submit Registration
    Registration Should Fail With Message  Password has to be at least 8 characters long and have numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  mismatchuser
    Set Password  password123
    Confirm Password  differentpassword
    Submit Registration
    Registration Should Fail With Message  Incorrect password confirmation


*** Keywords ***
Go To Register Page
    Go To  ${REGISTER_URL}

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
