import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Set the path to your Chrome WebDriver executable
webdriver_path = 'path/to/chromedriver'

# URL of your local WordPress site's admin panel
admin_url = 'http://localhost/test-site/wp-admin/'

# Start the Chrome browser with WebDriver
driver = webdriver.Chrome()

# Open the WordPress admin dashboard
driver.get(admin_url)

# Locate the username and password fields and submit button
username_field = driver.find_element(By.ID, 'user_login')
password_field = driver.find_element(By.ID, 'user_pass')
login_button = driver.find_element(By.ID, 'wp-submit')

# Input your username and password and click the login button
username_field.send_keys(wp_username)
password_field.send_keys(wp_password)
login_button.click()

# Wait for the admin panel to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'wpadminbar')))

# Go to the WP Dark Mode plugin settings
driver.get(admin_url + 'admin.php?page=wp-dark-mode-settings')

# Go to the "Switch Settings" tab
switch_settings_tab = driver.find_element(By.ID, 'wp_dark_mode_switch-tab')
switch_settings_tab.click()

# Wait for the "Custom" span element to be clickable
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Custom']")))

# Locate the "Custom" span element
custom_span = driver.find_element(By.XPATH, "//span[text()='Custom']")

# Click the "Custom" span to activate the custom value
custom_span.click()

# Wait for the "Custom" span element to be clickable
time.sleep(2)  # Adjust the sleep time as needed

# Locate the slider input element using JavaScript
slider_input = driver.execute_script('return document.querySelector("#wp_dark_mode_switch\\[switcher_scale\\]")')

# Use JavaScript to set the value of the slider to 220
driver.execute_script("arguments[0].value = '220'", slider_input)

# Trigger a change event to simulate user interaction
driver.execute_script("var event = new Event('change'); arguments[0].dispatchEvent(event);", slider_input)


# Wait for the "Save" button to become clickable
save_button = wait.until(EC.element_to_be_clickable((By.ID, 'save_settings')))

# Click the "Save" button
save_button.click()

# Wait for the changes to be saved (you can adjust the time as needed)
time.sleep(10)  # Wait for 10 seconds

# Close the browser
driver.quit()