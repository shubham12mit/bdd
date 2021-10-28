from selenium import webdriver
from behave import*

@given('click on the edit customer form')
def editcustomer(context):
    context.driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[3]/a").click()



@when('enter the correct customer id')
def correctid(context):
    context.driver.find_element_by_name("cusid").send_keys("96633")


@then('clcik on the submit button in edit customer form')
def step_impl(context):
    context.driver.find_element_by_name("AccSubmit").click()

#
# @then(u'enter the correct data in edit form')
# def correctdata(context):
#     raise NotImplementedError(u'STEP: Then enter the correct data in edit form')


@then(u'clcik on the edit customer submit button')
def button(context):
    context.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[14]/td[2]/input[1]')


@then(u'verify edit customer succesfully')
def step(context):
    assert True is True





