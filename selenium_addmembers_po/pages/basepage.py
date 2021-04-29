from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _base_url = ""

    def __init__(self, _driver_base: WebDriver = None):
        if _driver_base is None:
            # 避免driver重复初始化，第一次初始化的时候driver是空的，就进行初始化
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(15)
            print(self._base_url)
        else:
            self.driver = _driver_base

        if self._base_url != "":
            self.driver.get(self._base_url)

    # 元素定位    *解包元组 (by,name,pwd)
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入内容
    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    # 点击
    def on_click(self, loc):
        self.locator(loc).click()

    # def find(self, by, locator):
    #     return self.driver.find_element(by, locator)
    #
    # def find_and_click(self, by, locator):
    #     ele: WebElement = self.find(by, locator)
    #     ele.click()
    #     return ele
    #
    # def finds(self, by, locator):
    #     return self.driver.find_elements(by, locator)
