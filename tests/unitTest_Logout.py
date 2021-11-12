import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "testuser"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        #assert "Logged in"
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[6]/a").click()
        #ensure logout is successful
        time.sleep(3)

        try:
            # attempt to find the 'Login' button - if found, logged out
            elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[4]/a")

            assert True

        except NoSuchElementException:
            self.fail("Logout Failed - Button May not work")
            assert False

        time.sleep(3)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()