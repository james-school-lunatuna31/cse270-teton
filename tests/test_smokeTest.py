# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TestSmokeTest():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_siteHomepage1(self):
    self.driver.get("https://james-school-lunatuna31.github.io/cse270-teton/")
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title")
    assert len(elements) > 0
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_siteHomepage2(self):
    self.driver.get("https://james-school-lunatuna31.github.io/cse270-teton/")
    self.driver.set_window_size(1900, 1200)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "section > h3").text == "Welcome to the Teton Chamber of Commerce Signup Wizard!"
  
  def test_siteDirectoryPage3(self):
    self.driver.get("https://james-school-lunatuna31.github.io/cse270-teton/directory.html")
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
  
  def test_siteJoinPage4(self):
    self.driver.get("https://james-school-lunatuna31.github.io/cse270-teton/join.html")
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("James")
    self.driver.find_element(By.NAME, "lname").send_keys("Green")
    self.driver.find_element(By.NAME, "bizname").send_keys("Test")
    self.driver.find_element(By.NAME, "biztitle").send_keys("CEO")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
  def test_siteAdminPage5(self):
    self.driver.get("https://james-school-lunatuna31.github.io/cse270-teton/admin.html")
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("incorrect username")
    self.driver.find_element(By.ID, "password").send_keys("incorrect password")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
    assert len(elements) > 0
  