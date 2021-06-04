import allure

from api_lable_apiobject.apis.lablemanage import LableManage
from api_lable_apiobject.test_cases.utils import Utils


@allure.feature("标签管理测试")
class TestLableManage:

    def setup_class(self):
        data = Utils.open_file_load("../data/conf.yaml")
        print(data)
        corp_id = data['corp_id']['hogwarts']
        corp_secret = data['corp_secret']['department']
        self.lablemanage = LableManage(corp_id, corp_secret)
        ##准备数据
        self.tag_name = "霍格沃兹"
        self.tag_id = 16
        self.tag_upd_name = "霍格沃兹学院"

    def teardown(self):
        pass

    @allure.story("标签流程测试")
    def test_lable_flow(self):
        # 创建标签
        with allure.step("创建标签"):
            self.lablemanage.creat_lable(self.tag_id, self.tag_name)
        # 查看已创建的标签
        with allure.step("查看标签"):
            lable_info = self.lablemanage.get_lable(self.tag_id)
            print(lable_info)
            lable_name = Utils.base_jsonpath(lable_info, "$..tagname")
            self.lablemanage.log_info(lable_name)
            assert self.tag_name in lable_name
        # 更新标签
        with allure.step("更新标签"):
            self.lablemanage.update_lable(self.tag_id, self.tag_upd_name)
        # 查看更新后标签
        with allure.step("查看更新后标签"):
            lable_info = self.lablemanage.get_lable(self.tag_id)
            print(lable_info)
            lable_upd_name = Utils.base_jsonpath(lable_info, "$..tagname")
            self.lablemanage.log_info(lable_upd_name)
            assert self.tag_upd_name in lable_upd_name
        # 删除标签
        with allure.step("删除标签"):
            lable_info = self.lablemanage.delete_lable(self.tag_id)
            print(lable_info)
        # 查看是否删除
        with allure.step("查看删除结果"):
            # lable_info = self.lablemanage.get_lable(self.tag_id)
            # print(lable_info)
            # lable_id = Utils.base_jsonpath(lable_info,"$..tagid")
            # self.lablemanage.log_info(lable_id)
            assert lable_info['errcode'] == 0

        ##pytest --alluredir=./result
        ##allure generate --clean result -o result/html
