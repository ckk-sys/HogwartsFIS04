import logging

import requests


class BaseApi:
    # 设置 loging
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    logging.getLogger().setLevel(0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        ##添加日志信息
        return logging.info(msg)

    def send_api(self, req):
        self.log_info("----request------")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("----response------")
        self.log_info(r.json())
        return r
