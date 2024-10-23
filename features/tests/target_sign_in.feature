# Created by anooppottammal at 10/22/24
Feature: test for target sign in page

  Scenario:  user cannot log in with incorrect credential
    Given Open Target main page
    When click on the sign in button
    When click sigh in from side navigation menu
    When Enter incorrect email and password
    When Click log in button
    Then Verify that 'We can't find your account' message is shown


