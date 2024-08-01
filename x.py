from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup webdriver service
service = Service(ChromeDriverManager().install())

# Create a new instance of the browser driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the login page
driver.maximize_window()
driver.get('https://flip.id/')

# Find the elements by their IDs using WebDriverWait
wait = WebDriverWait(driver, 10)
 
# Locate and click the selector
css_selector = '.chakra-image.css-8s0vw3'  
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
element.click()

  # Locate and click the Flip Globe link
flip_globe_link = driver.find_element(By.XPATH, '//a[@role="group" and contains(@href, "flip-globe")]')
flip_globe_link.click()

# Scroll down to the bottom of the page
time.sleep(5)

# Locate and click the search bar button
search_bar_button = driver.find_element(By.XPATH, '//button[@class="chakra-menu__menu-button css-1l1pwnu"]')
search_bar_button.click()

# Wait for the search input field to be visible and input text
search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Cari negara atau kode mata uang"]')))
search_input.send_keys("united kingdom")


# Wait for the search results to appear and click the desired result
search_results_xpath = '//p[contains(@class, "chakra-text") and contains(text(), "United Kingdom")]'
search_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, search_results_xpath)))
search_result.click()

# Scroll down to the bottom of the page
time.sleep(5)

# Locate the input field for IDR amount
idr_input = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Masukkan nominal dalam IDR"]')))

# Clear the input field and enter the amount 50000
idr_input.clear()
idr_input.send_keys("50000")

# Scroll down to the bottom of the page
time.sleep(2)

# Wait for the exchange rate to be visible
exchange_rate = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class, "exchange-rate")]'))) 
    
# Wait for the service fee to be visible (if applicable)
service_fee = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class, "service-fee")]')))
    
# Extract values
exchange_rate_value = float(exchange_rate.text.replace('GBP', '').replace(',', '').strip())
service_fee_value = float(service_fee.text.replace('IDR', '').replace(',', '').strip())  # Adjust if needed

# Perform the calculation
idr_amount = 50000
calculated_gbp = idr_amount / exchange_rate_value
final_gbp = calculated_gbp - service_fee_value / exchange_rate_value

print(f"Exchange Rate: {exchange_rate_value}")
print(f"Service Fee: {service_fee_value}")
print(f"Calculated GBP: {calculated_gbp}")
print(f"Final GBP after service fee: {final_gbp}")

print(f"An error occurred: {e}")
# Print page source for debugging
print(driver.page_source)
