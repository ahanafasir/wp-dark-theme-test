# Import necessary modules from Selenium library
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Path to the ChromeDriver executable (you need to download this separately)
chrome_driver_path = '/path/to/chromedriver'

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Define the URL of the website you want to interact with
site_url = 'http://localhost/test-site'

# Navigate to the WordPress login page
driver.get(site_url + '/wp-login.php')

# Find the username and password fields on the login page
username_field = driver.find_element(By.ID, 'user_login')
password_field = driver.find_element(By.ID, 'user_pass')

# Enter your username and password into the respective fields
username_field.send_keys(wp_username)
password_field.send_keys(wp_password)

# Submit the login form by pressing the 'RETURN' key
password_field.send_keys(Keys.RETURN)

# Wait for a specific element to appear on the dashboard page, indicating a successful login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dashboard-widgets-wrap')))

print("Login Successful")

# Add a delay to keep the browser open for a few seconds (for debugging purposes)
time.sleep(10)  # Wait for 10 seconds

# Close the browser window
driver.close()
