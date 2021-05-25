import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 元素定位    *解包元组 (by,name,pwd)
    def locator(self, loc):
        logging.info('locator')
        logging.info(loc)
        return self.driver.find_element(*loc)

    # 输入内容
    def input(self, loc, text):
        logging.info('input')
        self.locator(loc).send_keys(text)

    # 点击
    def on_click(self, loc):
        logging.info('on_click')
        self.locator(loc).click()

    def swipe_find(self, add_ele, num=3):
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                ele = self.locator(add_ele)
                self.driver.implicitly_wait(5)
                return ele
            except:
                print('未找到')
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                # start_x: int, start_y: int, end_x: int, end_y: int,
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.2
                duration = 2000  # 单位ms
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == 2:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException()

    def back(self, num=3):
        for i in range(num):
            self.driver.back()
