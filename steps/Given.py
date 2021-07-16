from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
import sys
from behave import *


@given(u'I pass on boarding')
def check_app_launch(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()


@given(u'I am on home page')
def check_homepage_launch(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/action_search").is_displayed()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/action_notifications").is_displayed()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/action_cart").is_displayed()


@given(u'I am on basket page')
def check_homepage_launch(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/action_cart").click()


@given(u'I get the number of categories and write this number to console')
def print_number_of_categories(context):
    find_category_elements = context.driver.find_element_by_xpath(
        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab/android.widget.TextView").text
    total_categories = len(find_category_elements)
    print(total_categories)
