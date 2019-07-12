#@tag
Feature: Searching Mobile on google.com

  Background: Opening Google.com
    Given User is on homepage
    And open google.com

  @mobile
  Scenario Outline: Successfull search mobiles on google.com
    When user search for "<product>"
    And click on search button
    Then search result should come on the screen

    Examples: 
      | product  |
      | mobile |
      | computer  |
# Searching computers on google.com
#Given I want to write a step with <name>
#When I check for the <value> in step
#Then I verify the <status> in step
#
#Examples:
    #| name  |value | status |
    #| name1 |  5   | success|
    #| name2 |  7   | Fail   |
