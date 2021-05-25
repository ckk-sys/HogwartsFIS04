# 通讯录页
from appium.webdriver.common.mobileby import MobileBy

from appium_addmembers_po.pages.addmember_page import AddmemberPage
from appium_addmembers_po.pages.base_page import BasePage


class ContactPage(BasePage):
    add_ele = (MobileBy.XPATH, "//*[contains(@text,'添加成员')]")

    def addmember(self):
        self.swipe_find(self.add_ele, 4)
        return AddmemberPage(self.driver)
