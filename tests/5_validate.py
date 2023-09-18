# Import necessary modules from Selenium library
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Replace with your WordPress website URL
URL = 'http://localhost/test-site'

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the WordPress login page
driver.get(f'{URL}/wp-login.php')

# Find the username field and enter the username
username_field = driver.find_element(By.ID, 'user_login')
username_field.send_keys(wp_username)

# Find the password field and enter the password
password_field = driver.find_element(By.ID, 'user_pass')
password_field.send_keys(wp_password)

# Submit the login form by pressing Enter (since password_field.submit() is used)
password_field.submit()

# Wait for the dashboard to load (indicating a successful login)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dashboard-widgets-wrap')))

# Wait for the WordPress toolbar (admin bar) to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'wp-toolbar')))

# Find the switch element indicating WP Dark Mode status
switch = driver.find_element(By.CLASS_NAME, 'wp-dark-mode-active')

# Check if WP Dark Mode is enabled by checking if the switch is selected
if switch.is_selected():
    print('WP Dark Mode is not enabled')
else:
    print('WP Dark Mode is enabled')

# Add a delay to keep the browser open for a few seconds (for debugging)
time.sleep(10)  # Wait for 10 seconds

# Quit the WebDriver, closing the browser
driver.quit()
