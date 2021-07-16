Feature: As a user I want to add and remove products from to the wishlist

  Scenario: I add products to the wishlist and remove them, I should not see the added products
    Given I pass on boarding
    Given I am on home page
    Given I get the number of categories and write this number to console
    When I open a random category
    When I add 3 random products to wishlist via mini heart icon
    When I open the menu in the left
    When I go to My Wishlist and controls the page and products
    When I delete all of them from Wishlist
    Then I should not see the products I added to my wishlist