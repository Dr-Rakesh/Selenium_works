import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

# Load the questions from an Excel file
input_file = r"C:\Users\z004zn2u\Desktop\questions.xlsx"
df = pd.read_excel(input_file)

# Prepare the output DataFrame
output_data = {
    "Question": [],
    "Extracted Text": [],
    "Extracted URL": []
}

# Define the loop to go through each question
for index, row in df.iterrows():
    question = row['Question']
    
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize the WebDriver for Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Open the webpage
        driver.get("http://127.0.0.1:8000/")
        
        # Wait for the page to load and locate the email input field
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/input[1]")))
        
        # Enter the email
        email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/input[1]")
        email_input.send_keys("admin@siemens.com")
        
        # Enter the password
        password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/input[2]")
        password_input.send_keys("Fis@1234")
        
        # Click the login button
        login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]")
        login_button.click()
        
        # Wait for the next page to load
        time.sleep(20)
        
        # Find the question input field and submit the question from the Excel sheet
        question_input = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[2]/div/input[1]")
        question_input.send_keys(f"Question: {question}")
        
        # Click the image button to submit the question
        image_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[2]/div/img")
        image_button.click()
        
        # Wait for the response to load
        time.sleep(30)
        
        # Extract the response text
        text_container = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div")
        text_content = text_container.text
        
        # Extract the URL (if present)
        try:
            anchor_element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/a")
            url = anchor_element.get_attribute("href")
        except:
            url = None
        
        # Store the results in the output data
        output_data['Question'].append(question)
        output_data['Extracted Text'].append(text_content)
        output_data['Extracted URL'].append(url if url else "No URL found")
    
    except Exception as e:
        print(f"An error occurred for question: {question}, Error: {e}")
        output_data['Question'].append(question)
        output_data['Extracted Text'].append("Error occurred")
        output_data['Extracted URL'].append("Error occurred")
    
    finally:
        # Close the browser for the current iteration
        driver.quit()

print(f"Length of Question list: {len(output_data['Question'])}")
print(f"Length of Extracted Text list: {len(output_data['Extracted Text'])}")
print(f"Length of Extracted URL list: {len(output_data['Extracted URL'])}")

# Create a DataFrame from the output data and save it to an Excel file
output_df = pd.DataFrame(output_data)
output_file = "output_results.xlsx"
output_df.to_excel(output_file, index=False)

print(f"Process completed. Results saved to {output_file}")