import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HellowWorld(unittest.TestCase): 

  def setUp(self):
      return super().setUp()

  def test_hello_world(self):
      pass

  def tearDown(self):
      return super().tearDown()

if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello_world_report'))
  