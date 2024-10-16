# Created by anooppottammal at 9/24/24
Feature:test for target help ui elements

  Scenario: verify target help ui elements
    Given open target help page
    When  verify correct link for benefit cell
    Then  verify correct link shown


  Scenario: User can open and close Terms and Conditions from sign in page
    Given open target main page
    When click on the sign in button
    When click sigh in from side navigation menu
    When Store original window
    When Click on Target terms and conditions link
    Then Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And user can close current page
    And switch back to original
