# selenium_examples.py
'''
导入必要的库:

    webdriver、By、Keys、WebDriverWait、EC、time。

初始化 WebDriver:

    使用 Chrome 浏览器初始化 WebDriver。

打开一个网页:

    driver.get("https://www.google.com")。

查找元素:

    使用 find_element 和 By 类来定位页面元素。

输入文本并提交表单:

    send_keys 方法用于输入文本，send_keys(Keys.RETURN) 提交表单。

等待页面加载并检查标题:

    WebDriverWait 和 expected_conditions 用于等待特定条件满足。

查找和点击搜索结果:

    使用 find_elements 查找多个元素，点击第一个搜索结果链接。

截图:

    save_screenshot 方法保存页面截图。

获取页面源代码:

    page_source 属性获取页面 HTML 源代码。

导航到另一个 URL:

    使用 get 方法导航到另一个 URL。

前进和后退:

    back 和 forward 方法用于浏览器的前进和后退操作。

刷新页面:

    refresh 方法刷新当前页面。

关闭 WebDriver:

    quit 方法关闭 WebDriver 并结束会话。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # 初始化 WebDriver（以 Chrome 为例）
    driver = webdriver.Chrome()

    try:
        # 打开一个网页
        driver.get("https://www.google.com")
        print("Opened Google")

        # 查找元素
        search_box = driver.find_element(By.NAME, "q")
        print("Found search box")

        # 输入文本并提交表单
        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)
        print("Performed search")

        # 等待页面加载并检查标题
        WebDriverWait(driver, 10).until(EC.title_contains("Selenium Python"))
        print("Page title is:", driver.title)

        # 查找搜索结果
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        print(f"Found {len(results)} results")

        # 点击第一个搜索结果链接
        if results:
            first_result = results[0].find_element(By.TAG_NAME, "a")
            first_result.click()
            print("Clicked first search result")

            # 等待新页面加载
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            print("New page title is:", driver.title)

        # 截图
        driver.save_screenshot("screenshot.png")
        print("Screenshot taken")

        # 获取页面源代码
        page_source = driver.page_source
        print("Page source obtained")

        # 导航到另一个 URL
        driver.get("https://www.example.com")
        print("Navigated to example.com")

        # 前进和后退
        driver.back()
        print("Navigated back")
        driver.forward()
        print("Navigated forward")

        # 刷新页面
        driver.refresh()
        print("Page refreshed")

    finally:
        # 关闭 WebDriver
        driver.quit()
        print("WebDriver closed")

if __name__ == "__main__":
    main()
