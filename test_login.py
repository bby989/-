from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
import time
test_times=10
target_item="sauce-labs-bike-light"
for i in range (test_times):
    print(f"===第{i+1}次测试 ===")
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")  # 输入账号
driver.find_element(By.ID,"password").send_keys("secret_sauce")  # 输入密码
driver.find_element(By.ID,"login-button").click()  # 点击登录
time.sleep(3)
add_cart_btn_id=f"add-to-cart-{target_item}"
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(3)
driver.quit()
print("测试完成")

