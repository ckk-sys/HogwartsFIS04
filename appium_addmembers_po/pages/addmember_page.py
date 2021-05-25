# 添加成员页
from appium_addmembers_po.pages.base_page import BasePage
from appium_addmembers_po.pages.edit_member_page import EditMemberPage


class AddmemberPage(BasePage):

    def click_addmember_menual(self):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'输入添加')]").click()
        return EditMemberPage(self.driver)

    def verify_toast(self):
        return True
