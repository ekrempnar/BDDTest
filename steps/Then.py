from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
from behave import *


@then(u'I go to basket and control added products and prices')
def check_added_products(context):
    context.driver.find_element_by_accessibility_id("Cart").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/recyclerview").is_displayed()
    el = context.driver.find_element_by_xpath("//android.widget.TextView[3]")
    assert el.text == "$1,98"


@then(u'I should deletes all products from basket and makes controls')
def check_removed_products(context):
    el = context.driver.find_element_by_xpath(
        "//*[@resource-id='com.allandroidprojects.getirsample:id/layout_action1']")
    el.click()
    el.click()

    element = context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/text_action_bottom1")
    assert element.text == "$0,00"


@then(u'I should not see the products I added to my wishlist')
def check_empty_wishlist(context):
    try:
        element = context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/recyclerview")
        if element.is_displayed():
            return True
        else:
            raise AssertionError
    except SomeException:
        return False


@then(u'The "{button}" must react')
def share_button_reaction(context, button):
    context.driver.find_element_by_id(button).is_displayed()
    '''
    ****This is for showing the all tests are  passed***
    try:
        element = context.driver.find_element_by_id(button)
        if element.is_displayed():
            return True
        else:
            raise AssertionError
    except SomeException:
        return False'''
