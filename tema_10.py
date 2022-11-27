import unittest
import time
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStatusCode(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT,'Status Codes').click()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_url(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/status_codes'
        self.assertEqual(expected, actual, 'url error')

    def test_code_200(self):
        self.driver.find_element(By.LINK_TEXT, '200').click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/status_codes/200', 'not the same url'

    def test_code_301(self):
        self.driver.find_element(By.LINK_TEXT, '301').click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/status_codes/301', 'not the same url'