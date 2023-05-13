from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

comment = 'test'

box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "box")))
box.click()

frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="+1"]')))
driver.switch_to.frame(frame)

driver.find_element_by_xpath('//div[@onclick]').click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jsname="msEQQc"]/following-sibling::div//div[@g_editable="true"]')))
driver.execute_script("arguments[0].innerHTML='%s';" % comment, element)