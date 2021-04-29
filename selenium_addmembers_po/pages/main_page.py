from selenium.webdriver.common.by import By

from selenium_addmembers_po.pages.add_member_page import AddMember
from selenium_addmembers_po.pages.basepage import BasePage
from selenium_addmembers_po.pages.contact_page import Contact


# 首页
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    menu_ele = (By.ID, "menu_contacts")
    add_ele = (By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')

    def goto_contact(self):
        self.on_click(self.menu_ele)
        return Contact(self.driver)

    def add(self):
        self.on_click(self.add_ele)
        return AddMember(self.driver)
