# Created by anooppottammal at 9/19/24
Feature:  user can see target cart empty messege

  Scenario: Verify Cart is empty
    Given open target main page
    When click on the cart icon
    Then verify cart empty message shown

  Scenario: verify sign in page opened
    Given open target main page
    When click on the sign in button
    When click sigh in from side navigation menu
    Then verify sign in page opened

