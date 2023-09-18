# Import necessary modules from Selenium library
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Path to the ChromeDriver executable (you need to download this separately)
chrome_driver_path = '/path/to/chromedriver'

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Define the URL of the WordPress admin dashboard
site_admin_url = 'http://localhost/test-site/wp-admin/'

# Step 1: Login to the WordPress admin dashboard
driver.get(site_admin_url)  # Navigate to the WordPress admin login page
driver.find_element(By.ID, 'user_login').send_keys(wp_username)  # Locate username field and enter username
driver.find_element(By.ID, 'user_pass').send_keys(wp_password)  # Locate password field and enter password
driver.find_element(By.ID, 'wp-submit').click()  # Click the 'Log In' button

# Step 2: Navigate to the Plugins page in the WordPress admin dashboard
driver.get(site_admin_url + 'plugins.php')  # Navigate to the Plugins page

# Step 3: Check if the "WP Dark Mode" plugin is active
plugin_name = "WP Dark Mode"  # Replace with the exact name of the plugin
active_plugins = driver.find_elements(By.CSS_SELECTOR, 'tr.active')  # Find all active plugin rows
plugin_found = False  # Initialize a flag to check if the plugin is found

# Iterate through the list of active plugins to find the desired one
for plugin in active_plugins:
    if plugin_name in plugin.text:
        plugin_found = True  # Set the flag to indicate that the plugin is found
        break  # Exit the loop once the plugin is found

# Display a message based on whether the plugin was found
if plugin_found:
    print(f"The '{plugin_name}' plugin is active.")
else:
    print(f"The '{plugin_name}' plugin is not active.")

# Step 4: Wait for 10 seconds (for debugging purposes)
time.sleep(10)

# Step 5: Close the browser window and release resources
driver.quit()
