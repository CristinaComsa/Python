from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given(u'I am on Home page')
def step_impl(context):
    print(u'STEP: Given I am on Home page')
    context.driver.get('https://the-internet.herokuapp.com/')


@when(u'I click on Form Authentication')
def step_impl(context):
    print(u'STEP: When I click on Form Authentication')
    context.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()



@then(u'I am on Form Authentication page')
def step_impl(context):
    print(u'STEP: Then I am on Form Authentication page')
    assert context.driver.current_url == 'https://the-internet.herokuapp.com/login', 'url error'

@when(u'I click on File Download')
def step_impl(context):
    print(u'STEP: When I click on File Download')
    context.driver.find_element(By.LINK_TEXT, 'File Download').click()



@then(u'I am on File Download page')
def step_impl(context):
    print(u'STEP: Then I am on File Download page')
    assert context.driver.current_url == 'https://the-internet.herokuapp.com/download', 'url error'

@when(u'I click on Inputs')
def step_impl(context):
    print(u'STEP: When I click on Inputs')
    context.driver.find_element(By.LINK_TEXT, 'Inputs').click()

@then(u'I am on Inputs page')
def step_impl(context):
    print(u'STEP: Then I am on Inputs page')
    assert context.driver.current_url == 'https://the-internet.herokuapp.com/inputs', 'url error'
