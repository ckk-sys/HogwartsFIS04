from time import sleep

import yaml
from selenium import webdriver


class TestWeChat():

    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.find_element_by_id("menu_contacts").click()
        # 获取cookie
        cookie = driver.get_cookies()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    ##登录企业微信绕过扫码登录
    def test_login_wechat(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(5)
        self.driver.quit()
