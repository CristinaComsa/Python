Feature: Home page
  @form_authentication
  Scenario: test Form Authentication page
    Given I am on Home page
    When I click on Form Authentication
    Then I am on Form Authentication page

  @file_download
  Scenario: test File download page
    Given I am on Home page
    When I click on File Download
    Then I am on File Download page

  @inputs
  Scenario: test Inputs page
    Given I am on Home page
    When I click on Inputs
    Then I am on Inputs page

