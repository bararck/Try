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

# Wait for the element to be present and extract the text
try:
    # Wait and click the element with class 'chakra-text css-f6nt2g'
    clickable_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.chakra-text.css-f6nt2g")))
    clickable_element.click()
    
    # Wait and get the text from the element with class 'chakra-text css-f6nt2g'
    text_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.chakra-text.css-f6nt2g")))
    text = text_element.text
    print("Extracted text:", text)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the driver
    driver.quit()