from time import sleep

import pytest

from selenium_addmembers_po.config.file_load import open_file_load
from selenium_addmembers_po.pages.main_page import MainPage


class TestAddmember():

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    # 通讯录添加成员
    @pytest.mark.parametrize("utxt", open_file_load("../data/data.yaml"))
    def test_addmember1(self, utxt):
        # 链式调用
        # 主页-通讯录页面-点击添加成员-添加成员-获取成员信息
        ele = self.main.goto_contact(). \
            click_add_member(). \
            add_member(utxt["username"], utxt["acctid"], utxt["phone"]). \
            get_member()
        sleep(1)
        print(ele)
        assert utxt["phone"] in ele

    @pytest.mark.parametrize("utxt", open_file_load("../data/data.yaml"))
    def test_addmember2(self, utxt):
        # 链式调用
        # 主页-通讯录页面-点击添加成员-添加成员-获取成员信息
        ele = self.main.add(). \
            add_member(utxt["username"], utxt["acctid"], utxt["phone"]). \
            get_member()
        sleep(1)
        print(ele)
        assert utxt["phone"] in ele
