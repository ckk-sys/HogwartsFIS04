import pytest
import requests


class TestCreatLable:

    def setup_class(self):
        corp_id = "wwbea7ef49e49aae8e"
        corp_secret = "aLKnvfAKJF8THt6EOhpdC4QHVhXVx-AEb3AovcQxzIE"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.request("get", url)
        self.token = r.json()["access_token"]

    def teardown(self):
        pass

    @pytest.mark.parametrize("tag_id,tag_name", [
        [12, "霍格沃兹"], [13, "测码"], [14, "码尚"]
    ])
    def test_create_lables(self, tag_id, tag_name):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": tag_name,
            "tagid": tag_id
        }
        r = requests.request("post", url, json=data)
        assert r.json()["errcode"] == 0
