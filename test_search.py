from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()
# 打开百度首页
driver.get("https://www.baidu.com")

# 定位搜索框并输入关键词
search_box = driver.find_element(By.NAME, "wd")
search_box.send_keys("中国汉堡")

# 模拟按下回车键进行搜索
search_box.send_keys(Keys.RETURN)

# 验证搜索结果页面是否包含关键词
assert "中国汉堡" in driver.page_source

# 关闭浏览器
driver.quit()