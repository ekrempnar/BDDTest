from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import time
from behave import *


@when(u'I pass on boarding screens')
def pass_on_boarding_screens(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/btn_next").click()


@when(u'I change category to Baby Care')
def select_baby_care_category(context):
    context.driver.find_element_by_accessibility_id("Baby Care").click()


@when(u'I open a product detail from Baby Care category')
def open_product_detail(context):
    context.driver.find_element_by_xpath(
        "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]").click()


@when(u'I add Baby Care product to basket and return last page')
def add_basket(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/text_action_bottom1").click()
    context.driver.back()


@when(u'I change category to Snacks')
def select_snacks_category(context):
    context.driver.find_element_by_accessibility_id("Snacks").click()


@when(u'I open a product detail from Snacks category')
def open_product_detail(context):
    context.driver.find_element_by_xpath(
        "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]").click()


@when(u'I add Snacks product to basket and return last page')
def add_basket(context):
    context.driver.find_element_by_id("com.allandroidprojects.getirsample:id/text_action_bottom1").click()
    context.driver.back()


@when(u'I open a random category')
def open_random_category(context):
    context.driver.find_element_by_xpath(
        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]").click()


@when(u'I add 3 random products to wishlist via mini heart icon')
def add_three_products_to_wishlist(context):
    context.driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView").click()
    context.driver.find_element_by_xpath(
        "//android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView").click()
    context.driver.find_element_by_xpath(
        "//android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView").click()


@when(u'I open the menu in the left')
def open_left_menu(context):
    context.driver.find_element_by_accessibility_id("Open navigation drawer").click()


@when(u'I go to My Wishlist and controls the page and products')
def open_wishlist(context):
    context.driver.find_element_by_xpath("//android.support.v7.widget.LinearLayoutCompat[9]").click()


@when(u'I delete all of them from Wishlist')
def delete_from_wishlist(context):
    context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[1]/android.widget.LinearLayout/*[@resource-id='com.allandroidprojects.getirsample:id/ic_wishlist']").click()
    context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout/*[@resource-id='com.allandroidprojects.getirsample:id/ic_wishlist']").click()
    context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[1]/android.widget.LinearLayout/*[@resource-id='com.allandroidprojects.getirsample:id/ic_wishlist']").click()


@when(u'I open a product detail from a random category')
def open_random_product_detail(context):
    context.driver.find_element_by_xpath(
        "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]").click()
    context.driver.find_element_by_xpath(
        "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]").click()


@when(u'I click the button by "{btn_id}"')
def open_random_product_detail(context, btn_id):
    context.driver.find_element_by_id(btn_id).click()
