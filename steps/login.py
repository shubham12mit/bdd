from selenium import webdriver
from behave import *
@given('open crome browser')
def openbrowser(context):
    context.driver=webdriver.Chrome(executable_path="D:\shubham\driver\chromedriver_win32\chromedriver.exe")




@when('enter url')
def enterurl(context):
    context.driver.get("http://demo.guru99.com/v2/")



@when('verify guru99 logo')
def verifylogo(context):
    x=context.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/a/img").is_displayed()
    assert x is True


@then('enter username and password')
def usernamepassword(context):
    context.driver.find_element_by_name("uid").send_keys("mngr354857")
    context.driver.find_element_by_name("password").send_keys("UtEqUda")



@then('click on the log in button')
def clickonloginbutton(context):
    context.driver.find_element_by_name("btnLogin").click()


@then('verify guru99 welcome page')
def step_impl(context):
    x=context.driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee").is_displayed()
    assert x is True
