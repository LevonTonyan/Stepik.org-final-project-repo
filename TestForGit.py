from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
driver.find_element_by_id("book").click()

button = driver.find_element_by_id("solve")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

answer = driver.find_element_by_id("input_value")
answer_text = answer.text


y = calc(int(answer_text))
driver.find_element_by_id("answer").send_keys(y)

button.click()