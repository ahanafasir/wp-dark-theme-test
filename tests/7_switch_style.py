import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv() #load dotenv

wp_username = os.getenv("WP_USERNAME") #Fetch username into a variable from .env
wp_password = os.getenv("WP_PASSWORD") #Fetch password into a variable from .env

# Set the path to your ChromeDriver executable
chromedriver_path = '.test\chromedriver-win64\chromedriver.exe'

# Initialize the WebDriver
driver = webdriver.Chrome()  # You need to have ChromeDriver installed and in your PATH

# Replace with your WordPress admin URL and login credentials
admin_url = "http://localhost/test-site/wp-admin"

# Navigate to the WordPress admin login page
driver.get(admin_url)

# Log in to the admin dashboard
username_field = driver.find_element(By.ID, "user_login")
password_field = driver.find_element(By.ID, "user_pass")
login_button = driver.find_element(By.ID, "wp-submit")

username_field.send_keys(wp_username)
password_field.send_keys(wp_password)
login_button.click()

# Wait for the dashboard to load
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Dashboard"))

# Navigate to the WP Dark Mode plugin settings page
driver.get("http://localhost/test-site/wp-admin/admin.php?page=wp-dark-mode-settings")

# Switch to the "Switch Settings" tab
switch_settings_tab = driver.find_element(By.ID, "wp_dark_mode_switch-tab")
switch_settings_tab.click()

# Wait for the "Switch Settings" tab to load
wait.until(EC.presence_of_element_located((By.ID, "wp_dark_mode_switch-tab")))

# # Wait for the third switch style element to be clickable
# third_switch_style = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="wp_dark_mode_switch[switch_style]"][value="3"]')))

# # Click the third switch style
# third_switch_style.click()

try:
# Wait for the label element to be visible
    label_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'label.image-choose-opt.active'))
    )
    
    # Click the label element to select the radio button
    label_element.click()

    parent_element = driver.find_element(By.ID, 'wp_dark_mode_switch')

    # Find the button element with ID 'save_settings' within the parent element
    button_element = parent_element.find_element(By.ID, 'save_settings')

    button_element.click()
    

except Exception as e:
    print(f"An error occurred: {e}")


    
finally:
    # Wait for 10 seconds
    driver.implicitly_wait(10)
    # Close the web driver
    driver.quit()