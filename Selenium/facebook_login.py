import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class FacebookLogin(unittest.TestCase):
    @classmethod
    # Itentifies the setup of each the Chrome driver
    def setUp(inst):

        # create a new Chrome session
        inst.driver = webdriver.Chrome("C:/Users/Christine/Desktop/chromedriver.exe")

        # navigate to the application home page
        inst.driver.get("https://www.facebook.com")

    def test_1(self):
    	#--- Login ---
        # Finds the username and password fields
        self.email_field = self.driver.find_element_by_id('email') 
        self.password_field = self.driver.find_element_by_id('pass')

        # Entered the username and password
        # Update the Email and Password to the account needed
        self.email_field.send_keys('updateThisToTheCorrectEmail@something.com')
        self.password_field.send_keys('updateThisToTheCorrectPassword')

        # Selects the login button
        login = self.driver.find_element_by_id('loginbutton')
        time.sleep(3)
        login.click()
        
    	#--- Select Profile --- Working on getting this working
        # profile = self.driver.find_element_by_id('navItem_1392909668')
        # profile.click()

    	#--- Selects Photos --- Working on getting this working
        #photos = self.driver.find_element_by_id('u_fetchstream_3_7')
        #photos.click()        

    	#--- Log Out --- Working on getting this working
        # logout = self.driver.find_element_by_xpath('update')
        # logout.click()

    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

if __name__ == '__main__':
    # Generate an HTML report on test results---
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Facebook Login Testing Reports"))
