from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = "https://www.youtube.com/"
driver = webdriver.Chrome()
try:
    driver.get(url=url)
    driver.find_element(By.XPATH, '//*[@id="search"]')
    driver.refresh()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

