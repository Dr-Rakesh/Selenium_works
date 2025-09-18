from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://app-adt-00.azurewebsites.net/")

# Wait for 10 seconds to ensure the page loads
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/input[1]")))

# Find the email input field using its full XPath and type the email
email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/input[1]")
email_input.send_keys("admin@siemens.com")

# Find the password input field using its full XPath and type the password
password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/input[2]")
password_input.send_keys("Fis@1234")

# Find the login button using its full XPath and click it
login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]")
login_button.click()

# Wait for 10 seconds for the new page or content to load (after login)
time.sleep(2)

# Find the question input field using its full XPath and input the question
question_input = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[2]/div/input[1]")
question_input.send_keys("Question: What is team center")

# Find the image element (button) using its full XPath and click it
image_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[2]/div/img")
image_button.click()

# Wait for 10 seconds for the response to load
time.sleep(5)

# Find the text container using the full XPath to get the text
text_container = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div")
text_content = text_container.text

# Print the extracted text
print("Extracted Text:")
print(text_content)

# Find the anchor element using its full XPath
anchor_element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/a")

# Get the 'href' attribute value (the URL) from the anchor element
url = anchor_element.get_attribute("href")

# Print the URL if it exists
if url:
    print("\nExtracted URL:")
    print(url)
else:
    print("\nNo URL found.")

# Optional: wait for a few seconds before closing the browser
time.sleep(5)

# Close the browser
driver.quit()