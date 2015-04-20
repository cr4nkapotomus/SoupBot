#This is a proxy randomizer made for SoupBot, this helps emulate human traffic from all over the world since we can use selenium with webdriver to jump proxies
#This is also a work in progress. Cheers, Cr4_nk!

import random, requests
from selenium import webdriver

proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"} #Create list of proxies that do not need auth...
url = '' #This will be removed.
params = {"q" : ""} #This will be removed.

# load user agents and set headers
uas = LoadUserAgents()
ua = random.choice(uas)  # select a random user agent
headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

# make the request
r = requests.get(url, proxies=proxy,
    params=params, headers=headers)

	
	
#SELE WEB DRIVE CANNOT PROGRAMMATICALLY RANDOMIZE PROXIES, must use magic	

PROXY = "localhost:8080"

# Create a copy of desired capabilities object.
desired_capabilities = webdriver.DesiredCapabilities.chrome.copy()
# Change the proxy properties of that copy.
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

# you have to use remote, otherwise you'll have to code it yourself in python to 
# dynamically changing the system proxy preferences
driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities)



