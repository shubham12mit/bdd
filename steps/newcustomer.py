from selenium import webdriver
from behave import*
@given('click on the new customer')
def loginnescustomer(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[2]/a').click()


@when('enter the correct data')
def correctdata(context):
    context.driver.find_element_by_name("name").send_keys("shubham khadaskaRRR")
    context.driver.find_element_by_name("rad1").click()
    context.driver.find_element_by_name("dob").send_keys("12-01-1995")
    context.driver.find_element_by_name("addr").send_keys("golibar chowk nagpur")
    context.driver.find_element_by_name("city").send_keys("nagpur")
    context.driver.find_element_by_name("state").send_keys("maharashtra")
    context.driver.find_element_by_name("pinno").send_keys("440018")
    context.driver.find_element_by_name("telephoneno").send_keys("8956519720")
    context.driver.find_element_by_name("emailid").send_keys("khadaskar.s1RRR2@gmail.com")


@then('clcik on the submit button')
def submitbutton(context):
    context.driver.find_element_by_name("sub").click()
    context.driver.switch_to_alert().accept()

    # import time
    # time.sleep(30)

@then('verify new customer succesfully')
def stepimpl(context):
    assert True is True
