Feature: guru99login page test cases
  Background:
    Given open crome browser
    When enter url
    Then enter username and password
    Then click on the log in button

  Scenario: verify new customer page
      Given click on the new customer
      When enter the correct data
      Then clcik on the submit button
      And verify new customer succesfully

#  Scenario:verify edit customer page
#      Given click on the edit customer form
#      When enter the correct customer id
#      Then clcik on the submit button in edit customer form
#      Then clcik on the edit customer submit button
#      And verify edit customer succesfully

#  Scenario:verify new account page
#      Given click on the new account form
#      When enter the correct customer id
#      Then clcik on the submit button in edit customer form
#      Then clcik on the edit customer submit button
#      And verify edit customer succesfully