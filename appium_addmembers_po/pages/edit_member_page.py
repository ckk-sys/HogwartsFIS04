# 编辑成员页面
from appium.webdriver.common.mobileby import MobileBy

from appium_addmembers_po.pages.base_page import BasePage


class EditMemberPage(BasePage):
    name_ele = (MobileBy.XPATH, "//*[@text='必填']")
    phone_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    click_ele = (MobileBy.XPATH, "//*[@text='保存']")

    def edit_member(self, name, phone):
        from appium_addmembers_po.pages.addmember_page import AddmemberPage
        self.input(self.name_ele, name)
        self.input(self.phone_ele, phone)
        self.on_click(self.click_ele)
        return AddmemberPage(self.driver)
