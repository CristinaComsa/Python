Feature: Login Page
  As a user
  I am on login page

  @valid_credentials
  Scenario: enter valid credentials
    Given I am on Login Page
    When I type a valid user
    And I type a valid password
    And I click on login button
    Then I receive the "You logged into a secure area!" login message
    And I am on the secure page

  @valid_username
  Scenario: Fail login with valid username, wrong password
    Given I am on Login Page
    When I type a valid user
    And I type a wrong password
    And I click on login button
    Then I receive the "Your password is invalid!" login message
    And I am still on the login page

  @valid_password
  Scenario: Fail login with wrong username, valid password
    Given I am on Login Page
    When I type a wrong user
    And I type a valid password
    And I click on login button
    Then I receive the "Your username is invalid!" login message
    And I am still on the login page

