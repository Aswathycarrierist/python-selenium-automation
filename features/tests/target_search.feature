# Created by anooppottammal at 9/23/24
Feature: test for target search functionality

  Scenario:user can search for a product
    Given open target main page
    When search for pencil
    Then verify correct search result shown for pencil
    Then verify product pencil in URL

  Scenario:user can search for a product2
    Given open target main page
    When  search for mug
    Then  verify correct search result shown for mug


  Scenario Outline:user can search for a product3
    Given open target main page
    When search for <search_word>
    Then verify correct search result shown for <search_word>
    Examples:

      | search_word |
      | mug         |
      | notebook    |
      | pen         |


    