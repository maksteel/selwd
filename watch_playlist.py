# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, random
import configparser

class WatchPlaylist(unittest.TestCase):
    def waitForElementPresent(self, selector):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(selector))

    def setUp(self):
        self.parser = configparser.ConfigParser()
        self.parser.read('config.ini')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = self.parser.get('SITE', 'base_url')
        self.user = self.parser.get('SITE', 'user')
        self.password = self.parser.get('SITE', 'password')
	self.key_list = self.parser.get('SITE', 'key_list').split(" ")
        self.playlist = self.parser.get('SITE', 'playlist')
        self.limit = float(self.parser.get('SITE', 'limit'))
        self.verificationErrors = []
        self.accept_next_alert = True
       

    def waitRandom(self,limit=10):
	seconds = random.random() * limit
        print("Random wait " + str(seconds))
	time.sleep(seconds)	
    
    def test_watch_playlist(self):
        driver = self.driver
        
        print("Opening " + self.base_url)
        driver.get(self.base_url)
        
        print("Clicking Sign-in")
	driver.find_element_by_xpath("(//span[text()='Sign in'])").click()
        
        print("Entering email") 
        self.waitForElementPresent((By.ID, "identifierId"))
        driver.find_element_by_id("identifierId").clear()
        driver.find_element_by_id("identifierId").send_keys(self.user)
        self.waitRandom()
        driver.find_element_by_xpath("(//span[text()='Next'])").click()
        
        print("Entering password")
        self.waitForElementPresent((By.ID, "password"))
        self.waitRandom()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.password)
        #driver.find_element_by_css_selector("span.RveJvd.snByac").click()
        driver.find_element_by_xpath("(//span[text()='Next'])").click()
        
        random.shuffle(self.key_list,random.random)
        print("Searching " + " ".join(self.key_list))
        self.waitForElementPresent((By.ID,"masthead-search-term"))
        self.waitRandom()
        driver.find_element_by_id("masthead-search-term").send_keys(" ".join(self.key_list))
        self.waitRandom()
        driver.find_element_by_id("search-btn").click()
        self.waitRandom()
        
        print("Opening playlist")
        driver.find_element_by_link_text(self.playlist).click()
        
        print("Clicking shuffle")
        self.waitForElementPresent((By.XPATH,'//*[@title="Shuffle"]'))
        self.waitRandom()
        driver.find_element_by_xpath('//*[@title="Shuffle"]').click()
        self.waitRandom(limit=self.limit)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
