# Created by anooppottammal at 9/23/24
Feature: cart tests
  # Enter feature description here
Scenario: Verify Cart is empty
    Given open target main page
    When click on the cart icon
    Then verify cart empty message shown



  Scenario: user can add a product to the cart
    Given open target main page
    When search for mug
    And click on add to the cart button
    And confirm add to cart button from side navigation
    And click view cart and check out
