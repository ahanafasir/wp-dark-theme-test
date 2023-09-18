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

# Set the path to your ChromeDriver executable
chromedriver_path = '.test\chromedriver-win64\chromedriver.exe'

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get('http://localhost/test-site/wp-admin')

# Input Username
username = driver.find_element(By.ID, 'user_login')
username.send_keys(wp_username)

# Input Password
password = driver.find_element(By.ID, 'user_pass')
password.send_keys(wp_password)

# Click on the 'Log In' button
driver.find_element(By.ID, 'wp-submit').click()

# Wait for the dashboard to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dashboard-widgets-wrap')))

# Navigate to WP Dark Mode settings
driver.get('http://localhost/test-site/wp-admin/admin.php?page=wp-dark-mode-settings')

# Add a delay to keep the browser open for a few seconds (for debugging)
time.sleep(10)  # Wait for 10 seconds

# Close the driver
driver.quit()
