from api_lable_apiobject.apis.baseapi import BaseApi


class Wework(BaseApi):

    def __init__(self, corp_id, corp_secret):
        self.token = self.get_token(corp_id, corp_secret)

    def get_token(self, corp_id, corp_secret):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corp_id,
                "corpsecret": corp_secret
            }
        }

        r = self.send_api(req)
        print(r.json())
        return r.json()["access_token"]
