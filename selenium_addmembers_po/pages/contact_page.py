from time import sleep

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium_addmembers_po.pages.add_member_page import AddMember

# 通讯录页面
from selenium_addmembers_po.pages.basepage import BasePage


class Contact(BasePage):
    add_ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    name_ele = (By.ID, "username")

    def click_add_member(self):

        try:
            # *ele 解元组
            sleep(1)
            self.on_click(self.add_ele)
            # ele_num = len(self.driver.find_elements(self.name_ele))
            # print(ele_num)
        except(StaleElementReferenceException):
            print("没有找到元素")

        return AddMember(self.driver)

    def get_member(self):
        sleep(1)
        member_list = []
        print(member_list)
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        for value in eles:
            member_list.append(value.get_attribute("title"))
        print(member_list)
        return member_list
