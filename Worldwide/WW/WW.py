# imports

#silly selenium things
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests

#rng rng rng
import random



#configuring the chrome window, change the executable path to the path of your chrome driver
service = Service(executable_path=r"../cdriver/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless") #makes it so that you don't see the browser pop up
chrome_options.add_argument("--log-level=3") #clears all the clutter 
chrome_options.add_argument('--ignore-certificate-errors') #just in case necessary
chrome_options.add_argument('--allow-running-insecure-content') #just in case necessary
browser = webdriver.Chrome(service=service,options=chrome_options)

#list of words for the bot to google
words = ["swag","ohio","osama","ramen","capybara therapy"]

browser.get(f"https://www.google.com/search?q={random.choice(words)}")