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

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
webdriver_path = 'path/to/your/webdriver'

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Navigate to your WordPress admin login page
driver.get('http://localhost/test-site/wp-admin')

username_field = driver.find_element(By.ID, 'user_login')
password_field = driver.find_element(By.ID, 'user_pass')

username_field.send_keys(wp_username)
password_field.send_keys(wp_password)

# Find and click the login button
login_button = driver.find_element(By.ID, 'wp-submit')
login_button.click()

# Wait for the dashboard to load (adjust the wait time as needed)
dashboard_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'dashboard-widgets-wrap'))
)

# Navigate to the WP Dark Mode plugin settings page
driver.get('http://localhost/test-site/wp-admin/admin.php?page=wp-dark-mode-settings')

# Click on the Accessibility Settings tab
accessibility_tab = driver.find_element(By.ID, 'wp_dark_mode_accessibility-tab')
accessibility_tab.click()

# Find the keyboard shortcut toggle button and turn it off
keyboard_shortcut_toggle = driver.find_element(By.CLASS_NAME, 'keyboard_shortcut')
if not keyboard_shortcut_toggle.is_selected():
        keyboard_shortcut_toggle.click()

time.sleep(5)

# Find the "Save Changes" button (replace with actual ID or XPATH) and click it
save_changes_button = driver.find_element(By.ID, 'save_settings')  # Replace with actual ID or XPATH of Save Changes button

# Scroll to the "Save Changes" button to bring it into view
driver.execute_script("arguments[0].scrollIntoView();", save_changes_button)

save_changes_button.click()


# Wait for 10 seconds (adjust the wait time as needed)
time.sleep(10)

# Close the browser
driver.quit()
