from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Open the first webpage (Siemens login page)
driver.get("https://diswlogin.siemens.com/login?state=hKFo2SByUzBxWG5LaFZMeC1aRzhKdmJYczRsbGF0SEo2MEdCTaFupWxvZ2luo3RpZNkgRXFVZGRMc0I1UUNGQlJ6M2V5cVNmWkdLYmIxY0pqVlCjY2lk2SBoV3ZTa0NOT21nZXVCczJ5SWcwQUtHckF0UlZJcW5hcg&client")

# Wait for the email input field to be present
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/section/div/div/div/div[1]/div/form/div[2]/div/div/div/input")))

# Find the email input field using its full XPath and type the email
email_input = driver.find_element(By.XPATH, "/html/body/div/div/main/section/div/div/div/div[1]/div/form/div[2]/div/div/div/input")
email_input.send_keys("rakesh.rajagopalachary.ext@siemens.com")

# Find the login button using its full XPath and click it
login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/section/div/div/div/div[1]/div/form/div[4]/button")
login_button.click()

# Wait for the next page (post-login) to load by waiting for a specific element to appear
try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "new_element_xpath_after_login")))
    print("Login successful, new page loaded.")
except:
    print("Login process failed or took too long.")

# Now, open the new URL in the same browser window
driver.get("https://docs.sw.siemens.com/en-US/doc/282219420/PL20231129261301184.Configuration/xid1689921")

# Wait for the new page to load, or interact with elements on the new page as needed
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "specific_element_on_new_page_xpath")))
    print("New page loaded successfully.")
except:
    print("New page failed to load or took too long.")

# Close the browser
driver.quit()