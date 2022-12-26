from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'I am on Login Page')
def step_impl(context):
    print(u'STEP: Given I am on Login Page')
    context.driver.get('https://the-internet.herokuapp.com/login')


@when(u'I type a valid user')
def step_impl(context):
    print(u'STEP: When I type a valid user')
    context.driver.find_element(By.ID, 'username').send_keys('tomsmith')


@when(u'I type a valid password')
def step_impl(context):
    print(u'STEP: When I type a valid password')
    context.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')


@when(u'I click on login button')
def step_impl(context):
    print(u'STEP: When I click on login button')
    context.driver.find_element(By.TAG_NAME, 'i').click()


@then(u'I receive the "You logged into a secure area!" login message')
def step_impl(context):
    print(u'STEP: Then I receive the "You logged into a secure area!" login message')
    message = context.driver.find_element(By.ID, 'flash-messages').text
    assert "You logged into a secure area!" in message, 'login unsuccesfull'


@then(u'I am on the secure page')
def step_impl(context):
    print(u'STEP: Then I am on the secure page')
    assert context.driver.current_url == 'https://the-internet.herokuapp.com/secure', 'url not secure'


@when(u'I type a wrong password')
def step_impl(context):
    print(u'STEP: When I type a wrong password')
    context.driver.find_element(By.ID, 'password').send_keys('1234')


@then(u'I receive the "Your password is invalid!" login message')
def step_impl(context):
    print(u'STEP: Then I receive the "Your password is invalid!" login message')
    msg = context.driver.find_element(By.ID, 'flash').text
    assert "Your password is invalid!" in msg, 'login unsuccesfull'


@then(u'I am still on the login page')
def step_impl(context):
    print(u'STEP: Then I am still on the login page')
    assert context.driver.current_url == 'https://the-internet.herokuapp.com/login', 'not login url'


@when(u'I type a wrong user')
def step_impl(context):
    print(u'STEP: When I type a wrong user')
    context.driver.find_element(By.ID, 'username').send_keys('Cristina')


@then(u'I receive the "Your username is invalid!" login message')
def step_impl(context):
    print(u'STEP: Then I receive the "Your username is invalid!" login message')
    user_message = context.driver.find_element(By.ID, 'flash').text
    assert "Your username is invalid!" in user_message, 'login unsuccesfull'
