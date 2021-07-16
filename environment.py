import os
from appium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from appium.webdriver.common.touch_action import TouchAction
import time

def before_feature(context, feature):
    caps = {}
    caps["app"] = "C:/Users/ekrem/Projects/BDDTest/sampleGetir.apk"
    caps["deviceName"] = "2812652218000537"
    caps["platformName"] = "Android"
    caps["ensureWebviewsHavePages"] = True

    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    context.driver.implicitly_wait(5)

    for scenario in feature.walk_scenarios():
            patch_scenario_with_autoretry(scenario, max_attempts=2)

def before_scenario(context, scenario):
    context.driver.reset()
    context.driver.implicitly_wait(5)
