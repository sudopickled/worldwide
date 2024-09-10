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
import time
import random

path = "../output/output.png"

#configuring the chrome window, change the executable path to the path of your chrome driver
service = Service(executable_path=r"../cdriver/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless") #makes it so that you don't see the browser pop up
chrome_options.add_argument("--log-level=3") #clears all the clutter 
chrome_options.add_argument('--ignore-certificate-errors') #just in case necessary
chrome_options.add_argument('--allow-running-insecure-content') #just in case necessary
chrome_options.add_argument("window-size=1920,1080")
browser = webdriver.Chrome(service=service,options=chrome_options)

#list of words for the bot to google
words = ["youtube.com", "google.com"]

browser.get(f"https://{random.choice(words)}")

browser.save_screenshot(path)

#plants = driver.find_elements(By.TAG_NAME, "body")
#print(plants)