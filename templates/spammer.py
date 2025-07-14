from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random, time

def spam_form(form_url, yes_percent=70, repeat=5):
    chrome_path = "PATH/TO/chromedriver"
    service = Service(chrome_path)

    for _ in range(repeat):
        driver = webdriver.Chrome(service=service)
        driver.get(form_url)
        time.sleep(2)

        # Ví dụ: chọn "Có" hoặc "Không" dựa vào phần trăm
        if random.randint(1, 100) <= yes_percent:
            driver.find_element(By.XPATH, '//div[@data-value="Có"]').click()
        else:
            driver.find_element(By.XPATH, '//div[@data-value="Không"]').click()

        # Gửi biểu mẫu
        driver.find_element(By.XPATH, '//span[text()="Gửi"]').click()
        time.sleep(2)
        driver.quit()
