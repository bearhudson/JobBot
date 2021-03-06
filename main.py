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
driver.get("https://www.linkedin.com/home/")
login_1 = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
login_1.click()
login_user = driver.find_element(By.ID, 'username')
login_user.send_keys(f"{USER_LOGIN}")
login_pass = driver.find_element(By.ID, 'password')
login_pass.send_keys(f"{USER_PASSWORD}")
time.sleep(1)
login2 = driver.find_element(By.CLASS_NAME, "login__form_action_container")
login2.click()
time.sleep(1)
driver.get("https://www.linkedin.com/jobs/")
time.sleep(1)
job_search = driver.find_element(By.CLASS_NAME, 'jobs-home-soho-search-card__truncated-text')
job_search.click()
job_list = driver.find_elements(By.XPATH, "/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/div[1]/div[2]/div[1]/a"

in_loop = True
while in_loop:
    for job in job_list:
        print(job.text.strip())
    in_loop = False

driver.quit()
