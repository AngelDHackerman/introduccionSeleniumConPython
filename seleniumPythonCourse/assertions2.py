import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # Esto nos permitira hacer exceptiones para nuestras assertions.


class AssertionsTest(unittest.TestCase):

  def setUp(self):
      self.driver = webdriver.Chrome(executable_path = './chromedriver')
      driver = self.driver
      driver.implicitly_wait(30) # hace que espere 30 segundos
      driver.maximize_window()
      driver.get('http://demo-store.seleniumacademy.com/')

  def tearDown(self):
    self.driver.quit()