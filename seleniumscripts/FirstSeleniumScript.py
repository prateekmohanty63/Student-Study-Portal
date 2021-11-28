from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver=webdriver.Chrome(executable_path="C:\\Users\\BRBCO\\Downloads\\chromedriver_win32\\chromedriver.exe",chrome_options=options)




# Automated testing for youtube
driver.get("http://127.0.0.1:8000/youtube")
driver.find_element_by_name("text").send_keys("Selenium")
driver.find_element_by_class_name("btn").click()

time.sleep(0.3)
#automated testing for wikipedia
driver.get("http://127.0.0.1:8000/wiki")
driver.find_element_by_name("text").send_keys("Selenium")
driver.find_element_by_class_name("btn").click()

time.sleep(0.3)

#automated testing for books
driver.get("http://127.0.0.1:8000/books")
driver.find_element_by_name("text").send_keys("Selenium")
driver.find_element_by_class_name("btn").click()

time.sleep(0.3)

#automated testing for Todo
driver.get("http://127.0.0.1:8000/todo")
driver.find_element_by_name("title").send_keys("Walk daily")
driver.find_element_by_class_name("btn").click()



driver.get("https://127.0.0.8000/login")
driver.find_element_by_name("username").send_keys("root")
driver.find_element_by_name("password").send_keys(1234)
driver.find_element_by_class_name("btn").click()

time.sleep(0.3)


# driver.get("https://127.0.0.8000/login")
# driver.find_element_by_name("username").send_keys("root")
# driver.find_element_by_name("password").send_keys(1234)
# driver.find_element_by_class_name("btn").click()


#driver.find_element_by_id("searchField").send_keys("Movies")



