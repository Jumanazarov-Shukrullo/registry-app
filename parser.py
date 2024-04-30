import json
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
import lxml


def init_driver(driver_path, url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-popup-blocking')
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    return driver


def get_data(driver):
    driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[2]/div[2]").click()
    select = Select(driver.find_element(By.ID, "table_length"))
    select.select_by_visible_text(str(100))
    datum = []
    for j in range(1, 106):
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find('table', class_='dataTable no-footer')
        table_body = table.find('tbody')
        rows = table_body.findAll('tr')
        for row in rows:
            r = row.findAll('td')
            data = []
            for i in r:
                if len(i.text) == 0:
                    data.append(None)
                else:
                    data.append(i.text)
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
        try:
            driver.find_element(By.ID, 'dataset_table_next').click()
        except selenium.common.exceptions.StaleElementReferenceException as e:
            driver.find_element(By.ID, 'dataset_table_next').click()
    return datum


def save_to_json(datum):
    with open("data.json", "a") as file:
        json.dump(datum, file, indent=4, ensure_ascii=False)


def main():
    driver_path = '/usr/bin/chromedriver'
    url = "https://opendata.mkrf.ru/opendata/7705851331-heritage_safekeeping_licenses"
    driver = init_driver(driver_path, url)
    data = get_data(driver)
    save_to_json(data)


if __name__ == "__main__":
    main()
