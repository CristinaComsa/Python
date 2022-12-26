Feature: Secure Page
  As a user
  I am on secure page

  @secure_page
  Scenario: Enter valid credentials
    Given I am on Login page
    When I type a valid username
    And I type a valid Password
    And I click on Login button
    And I receive the "You logged into a secure area!" login message
    And I verify if it is displayed
    Then I click on Logout button
    And I am again on the login page
