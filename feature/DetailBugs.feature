Feature: As a user I want to add a product to my wishlist and share a product by using detail wishlist and share buttons

  Scenario Outline: I go to a product detail and click Wishlist and Share buttons, I should see this product in the my wishlist and Share button has a reaction
    Given I pass on boarding
    Given I am on home page
    When I open a product detail from a random category
    When I click the button by "<id>"
    Then The "<button>" must react
    Examples:
      | id                                                   | button                                               |
      | com.allandroidprojects.getirsample:id/layout_action1 | com.allandroidprojects.getirsample:id/layout_action1 |
      | com.allandroidprojects.getirsample:id/layout_action3 | com.allandroidprojects.getirsample:id/layout_action3 |
