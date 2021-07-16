Feature: As a user I want to add and remove products from to the basket

  Scenario: I add products to the basket and remove them, I should not see the added products
    Given I pass on boarding
    Given I am on home page
    When I change category to Snacks
    When I open a product detail from Snacks category
    When I add Snacks product to basket and return last page
    When I change category to Baby Care
    When I open a product detail from Baby Care category
    When I add Baby Care product to basket and return last page
    Then I go to basket and control added products and prices
    Then I should deletes all products from basket and makes controls





