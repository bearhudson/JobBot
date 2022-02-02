from environs import *
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

selenium_service = Service("/home/brian/bin/chromedriver")
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)
driver.get("file:///home/brian/PycharmProjects/JobBot/jobs.html")
job_list = driver.find_elements(By.XPATH, "/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li")

in_loop = True

while in_loop:
    for job in job_list:
        print(job.text)
    in_loop = False
