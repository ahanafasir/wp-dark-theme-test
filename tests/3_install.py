# Import necessary modules from Selenium library
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Set the path to your ChromeDriver executable
chromedriver_path = '.test\chromedriver-win64\chromedriver.exe'

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Replace with your WordPress site URL and login credentials
site_url = 'http://localhost/test-site'
username = wp_username
password = wp_password

# Go to the WordPress login page
driver.get(f'{site_url}/wp-login.php')

# Log in
driver.find_element(By.ID, 'user_login').send_keys(username)  # Locate the username field and enter the username
driver.find_element(By.ID, 'user_pass').send_keys(password)  # Locate the password field and enter the password
driver.find_element(By.ID, 'wp-submit').click()  # Click the 'Log In' button

# Wait for the dashboard to load
dashboard_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'dashboard-widgets-wrap'))
)

# Go to the Plugins page
driver.get(f'{site_url}/wp-admin/plugins.php')

# Check if WP Dark Mode is active
if 'Deactivate' in driver.page_source:
    print('WP Dark Mode is active')
    
    # Navigate to WP Dark Mode settings (you may need to adjust this based on your plugin's structure)
    driver.get(f'{site_url}/wp-admin/options-general.php?page=wp-dark-mode-settings')
    
    # Enable dark mode (you may need to adjust this based on your plugin's structure)
    # Assuming there's a checkbox for enabling dark mode with ID 'dark-mode-toggle'
    dark_mode_toggle = driver.find_element(By.ID, 'dark-mode-toggle')
    if not dark_mode_toggle.is_selected():
        dark_mode_toggle.click()
        print('Dark mode is enabled')
else:
    # Add a new plugin
    add_new_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Add New')
    add_new_button.click()

    # Search for WP Dark Mode in the plugin store
    search_input = driver.find_element(By.ID, 'search-plugins')
    search_input.send_keys('WP Dark Mode')
    search_input.send_keys(Keys.RETURN)

    # Wait for WP Dark Mode to appear in the search results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "WP Dark Mode")]'))
    )

    # Install and activate WP Dark Mode
    install_button = driver.find_element(By.CLASS_NAME, "install-now")
    install_button.click()

    # Wait for installation to complete
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Activate")]'))
    )

    activate_button = driver.find_element(By.CLASS_NAME, "activate-now")
    activate_button.click()

    # Wait for activation to complete
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Deactivate")]'))
    )

    print('WP Dark Mode is activated')

    # Navigate to WP Dark Mode settings
    driver.get(f'{site_url}/wp-admin/options-general.php?page=wp-dark-mode-settings')

    # Enable dark mode (you may need to adjust this based on your plugin's structure)
    dark_mode_toggle = driver.find_element(By.ID, 'dark-mode-toggle')
    if not dark_mode_toggle.is_selected():
        dark_mode_toggle.click()
        print('Dark mode is enabled')

# Add a delay to keep the browser open for a few seconds (for debugging)
time.sleep(10)  # Wait for 10 seconds

# Close the browser when done
driver.quit()
