from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.google.com")
time.sleep(random.uniform(2, 3))

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Top AI tools 2025")
search_box.send_keys(Keys.RETURN)
time.sleep(random.uniform(2, 4))

results = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf a')
print("🔍 Top 5 Google Results:\n")
for i in range(min(5, len(results))):
    print(f"{i+1}. {results[i].text}\n   {results[i].get_attribute('href')}\n")

driver.quit()
