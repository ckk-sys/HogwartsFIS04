# 添加成员页面
from selenium.webdriver.common.by import By

from selenium_addmembers_po.pages.basepage import BasePage


class AddMember(BasePage):
    # 定位页面元素
    username_ele = (By.ID, "username")
    acctid_ele = (By.ID, "memberAdd_acctid")
    phone_ele = (By.ID, "memberAdd_phone")
    click_ele = (By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self, name, acctid, phone):
        # 避免循环导入；局部导入
        from selenium_addmembers_po.pages.contact_page import Contact
        self.input(self.username_ele, name)
        self.input(self.acctid_ele, acctid)
        self.input(self.phone_ele, phone)
        self.on_click(self.click_ele)
        return Contact(self.driver)
