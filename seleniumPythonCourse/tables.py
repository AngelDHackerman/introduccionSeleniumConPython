from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
from time import sleep

class Tables(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path= "./chromedriver")
    driver = self.driver
    driver.get("http://the-internet.herokuapp.com")
    driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

  def test_sort_tables(self):
    pass

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main()