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

# Set your WordPress admin URL and credentials
admin_url = "http://localhost/test-site/wp-admin"

# Set the path to your ChromeDriver executable
chromedriver_path = '.test\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome()

# Navigate to the WordPress admin login page
driver.get(admin_url)

# Log in to the admin dashboard
username_input = driver.find_element(By.ID, "user_login")
password_input = driver.find_element(By.ID, "user_pass")
login_button = driver.find_element(By.ID, "wp-submit")

username_input.send_keys(wp_username)
password_input.send_keys(wp_password)
login_button.click()

# Wait for the dashboard to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "dashboard-widgets-wrap")))

# Navigate to the WP Dark Mode plugin settings
driver.get(admin_url + "/admin.php?page=wp-dark-mode-settings")

# Switch to the Animation tab
animation_tab = driver.find_element(By.ID, "wp_dark_mode_animation-tab")
animation_tab.click()

#Toggle animation
switch = driver.find_element(By.CLASS_NAME, 'toggle_animation')
if not switch.is_selected():
    switch.click()

# Find the animation effect drop-down and select "pulse"
animation_effect_dropdown = driver.find_element(By.ID, "wp_dark_mode_animation[animation]")
animation_effect_dropdown.send_keys("Pulse")

time.sleep(5) # 5secs delay

parent_element = driver.find_element(By.ID, 'wp_dark_mode_animation')

# Find the button element with ID 'save_settings' within the parent element
button_element = parent_element.find_element(By.ID, 'save_settings')

button_element.click()

# Wait for 10 seconds before closing the browser
time.sleep(10)

# Close the browser
driver.quit()


