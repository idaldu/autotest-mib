import self as self
import re
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "09231FDD4006UK",
        "app": "C:\\Users\\unrea\\PycharmProjects\\mib-test\\app_binaries\\mib-prod.apk",
    }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Войти').click()
e = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Номер телефона"]')
e.click()
e.clear()
e.send_keys('557227828')

e = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Пароль"]')
e.click()
e.clear()
e.send_keys('Colvir456&&')

driver.hide_keyboard()
e = driver.find_element(By.XPATH, "(//android.view.View[@content-desc=\"Войти\"])[2]")
driver.implicitly_wait(1)
e.click()

driver.implicitly_wait(4)
for i in range(8):
    driver.implicitly_wait(0.3)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '5').click()
    driver.implicitly_wait(0.3)

driver.implicitly_wait(1)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(516, 48)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(537, 1760)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.implicitly_wait(8)
word = driver.find_element(By.ID, "android:id/message_text").text
pattern = re.compile(r'\w+')
code_sms = pattern.findall(word)[0]
print(code_sms)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(502, 2102)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(509, 48)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.implicitly_wait(1)
digits = []
for symbol in word:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
for i in range(6):
    driver.press_keycode(digits[i] + 7)

driver.hide_keyboard()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подтвердить').click()

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'СМС подтверждение').click()