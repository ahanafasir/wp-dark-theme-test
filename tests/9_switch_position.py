import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Set the path to your ChromeDriver executable
chromedriver_path = '.test\chromedriver-win64\chromedriver.exe'

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Replace with your WordPress admin URL, username, and password
admin_url = "http://localhost/test-site/wp-admin"

# Navigate to the WordPress admin login page
driver.get(admin_url)

# Locate the username and password fields, and log in
username_field = driver.find_element(By.ID, "user_login")
password_field = driver.find_element(By.ID, "user_pass")
login_button = driver.find_element(By.ID, "wp-submit")

username_field.send_keys(wp_username)
password_field.send_keys(wp_password)
login_button.click()

# Wait for the dashboard to load (you may need to adjust the wait time)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard-widgets-wrap")))

# Navigate to the WP Dark Mode plugin settings page
dark_mode_settings_url = "http://localhost/test-site/wp-admin/admin.php?page=wp-dark-mode-settings"
driver.get(dark_mode_settings_url)

# Go to the "Switch Settings" tab
switch_settings_tab = driver.find_element(By.ID, 'wp_dark_mode_switch-tab')
switch_settings_tab.click()

# Wait for the settings page to load (you may need to adjust the wait time)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wp_dark_mode_switch[switcher_position]")))

# Locate and change the floating switch position to "Bottom Left"
switch_settings_dropdown = driver.find_element(By.ID, "wp_dark_mode_switch[switcher_position]")
switch_settings_dropdown.send_keys("Left Bottom")

# Wait for 5 seconds (or as needed)
time.sleep(5)


# Find the "Save Changes" button (replace with actual ID or XPATH) and click it
save_changes_button = driver.find_element(By.ID, 'save_settings')  # Replace with actual ID or XPATH of Save Changes button

# Scroll to the "Save Changes" button to bring it into view
driver.execute_script("arguments[0].scrollIntoView();", save_changes_button)

# Click the "Save Changes" button
save_changes_button.click()


# Wait for 10 seconds (or as needed)
time.sleep(10)

# Close the browser
driver.quit()
