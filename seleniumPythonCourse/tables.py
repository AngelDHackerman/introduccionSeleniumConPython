from email import header
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
    driver = self.driver

    tables_data = [[] for i in range(5 + 1)]  # usamos un list comprenhension
    print(tables_data)

    for i in range(5):
      header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i  + 1}]/span')  # con esta {i} podemos iterar sobre las opciones que nos da la tablar de nuestra pagina
      tables_data[i].append(header.text)

      for j in range(4):
        row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[1]')  # // //*[@id="table1"]/tbody/tr[2]/td[1]
        tables_data[i].append(row_data.text)

    print(tables_data)

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main()