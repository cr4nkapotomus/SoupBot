#This is script 7, which runs through a selenium link clickthrough, this script will
#Hopefully run through a proxy and 'analytics' to make traffic look more human
#Cheers! Cr4_nk!

import time, subprocess
#from twisted.internet import reactor
#from twisted.internet import protocol
#from twisted.python import log
#from twisted.words.protocols import irc
from selenium import webdriver

driver = webdriver.Chrome('/home/soupersalad/Botnwt/chromedriver')
driver.get('http://www.google.com/xhtml');
time.sleep(2) #This allows user to see something
search_box = driver.find_element_by_name('q')
search_box.send_keys('EDIT THIS IN RELATION TO SETUP')
search_box.submit()
time.sleep(2) #This also allows user to see something
			
link = driver.find_element_by_link_test('EDIT THIS IN RELATION TO SETUP// This will be verbatim to link text')
link.click()
			
time.sleep(2) #Wait
			
link = driver.find_element_by_link_test('EDIT THIS IN RELATION TO SETUP// This will be verbatim to link text')
link.click()
			
time.sleep(2) #Wait
			
driver.quit() #Clears out webdriver, closes chrome, etc..)