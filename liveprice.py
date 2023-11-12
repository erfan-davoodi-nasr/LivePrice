# pip install selenium webdriver_manager datetime
# this code works just in google chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime

def get_price():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://nobitex.ir/usdt/")

    price = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/div[3]/div/section[1]/div/div[2]/div[2]/div[2]/span[2]')

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f'Current Time: {current_time}, Live price {price.text}')

    driver.close()

get_price()
