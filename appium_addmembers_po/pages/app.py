from appium import webdriver

from appium_addmembers_po.pages.base_page import BasePage
from appium_addmembers_po.pages.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            caps = {

                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                ##不停止app
                # "dontStopAppOnReset": "true",
                ##默认已经登录或者不重新初始化
                "noReset": "true",
                'settings[waitForIdleTimeout]': 0  # 等待页面空闲的时间

            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            # 启动app
            self.driver.launch_app()
            # 启动过程中启动其他应用
            # self.driver.start_activity()
        return self

    def restart(self):
        # 关闭
        self.driver.close()
        # 启动app
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
