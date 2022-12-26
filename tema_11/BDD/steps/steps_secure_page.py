from behave import given, when, then
from selenium.webdriver.common.by import By

@when('I type a valid username')
def step_impl(context):
    print('STEP: When I type a valid username')
    context.driver.find_element(By.ID, 'username').send_keys('tomsmith')

@when('I receive the "You logged into a secure area!" login message')
def step_impl(context):
    print('STEP: When I receive the "You logged into a secure area!" login message')
    message = context.driver.find_element(By.ID, 'flash').text
    assert "You logged into a secure area!" in message, 'not on the secure page'

@when('I verify if it is displayed')
def step_impl(context):
    print('STEP: When I verify if it is displayed')
    txt = context.driver.find_element(By.ID, 'flash')
    assert txt.is_displayed(), 'text not diplayed'


@then('I click on Logout button')
def step_impl(context):
    print('STEP: Then I click on Logout button')
    context.driver.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()


@then('I am again on the login page')
def step_impl(context):
    print('STEP: Then I am again on the login page')
    assert context.driver.current_url == 'https://the-internet.herokuapp.com/login', 'url error'
