from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, random

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def main():
    driver = get_driver()
    driver.get("https://www.google.com")
    time.sleep(random.uniform(2, 3))
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Top AI tools 2025")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.save_screenshot("screenshot.png")
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    print("🔍 Top 5 Google Results:\n")
    for i, result in enumerate(search_results[:5]):
        title = result.find_element(By.CSS_SELECTOR, "h3").text
        link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        print(f"{i+1}. {title}\n   {link}\n")
    driver.quit()

if __name__ == "__main__":
    main()
