import json
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
import lxml


# Function to initialize the WebDriver
def init_driver(driver_path, url):
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--no-sandbox')  # Disable sandbox mode
    chrome_options.add_argument('--disable-popup-blocking')  # Disable popup blocking

    # Create a WebDriver service
    service = Service(driver_path)
    
    # Create a WebDriver instance with the configured options and service
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the specified URL in the WebDriver
    driver.get(url)
    
    return driver


# Function to extract data from the webpage
def get_data(driver):
    # Click on the element to show more entries
    driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[2]/div[2]").click()
    
    # Select the number of entries to display (100 entries per page)
    select = Select(driver.find_element(By.ID, "table_length"))
    select.select_by_visible_text(str(100))
    
    datum = []
    # Iterate through each page of the table (106 pages in total)
    for j in range(1, 106):
        # Parse the HTML of the current page using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find('table', class_='dataTable no-footer')
        table_body = table.find('tbody')
        rows = table_body.findAll('tr')
        # Extract data from each row of the table
        for row in rows:
            r = row.findAll('td')
            data = []
            # Extract text from each cell of the row
            for i in r:
                if len(i.text) == 0:
                    data.append(None)
                else:
                    data.append(i.text)
            # Append the extracted data to the datum list as a dictionary
            datum.append({
                "fullname": data[0],
                "abbreviated_name": data[1],
                "licence_number": data[2],
                "inn": data[3],
                "date_of_registration": data[4],
                "address": data[5],
                "deadline": data[6],
                "status": data[7],
                "termination_date": data[8],
            })
        # Click on the next page button to navigate to the next page
        try:
            driver.find_element(By.ID, 'dataset_table_next').click()
        except selenium.common.exceptions.StaleElementReferenceException as e:
            driver.find_element(By.ID, 'dataset_table_next').click()
    return datum


# Function to save extracted data to a JSON file
def save_to_json(datum):
    with open("data.json", "a") as file:
        json.dump(datum, file, indent=4, ensure_ascii=False)


# Main function
def main():
    # Path to the chromedriver executable
    driver_path = '/usr/bin/chromedriver'
    
    # URL of the webpage containing the data
    url = "https://opendata.mkrf.ru/opendata/7705851331-heritage_safekeeping_licenses"
    
    # Initialize the WebDriver
    driver = init_driver(driver_path, url)
    
    # Extract data from the webpage
    data = get_data(driver)
    
    # Save extracted data to a JSON file
    save_to_json(data)


if __name__ == "__main__":
    main()
