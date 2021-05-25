from faker import Faker

from appium_addmembers_po.pages.app import App
from appium_addmembers_po.utils.contact import Contact


class TestAddMember:

    def setup_class(self):
        # self.faker = Faker('zh_CN')
        # 启动app
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def test_addmember(self):
        result = self.main.goto_contact().addmember() \
            .click_addmember_menual().edit_member(Contact.get_name(), Contact.get_phone()) \
            .verify_toast()
        assert result
