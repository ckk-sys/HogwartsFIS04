# 主页
from appium.webdriver.common.mobileby import MobileBy

from appium_addmembers_po.pages.base_page import BasePage
from appium_addmembers_po.pages.contact_page import ContactPage


class MainPage(BasePage):
    contact_ele = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact(self):
        self.on_click(self.contact_ele)
        return ContactPage(self.driver)
