from api_lable_apiobject.apis.wework import Wework


class LableManage(Wework):

    # 创建标签
    def creat_lable(self, tag_id, tag_name):
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json": {
                "tagname": tag_name,
                "tagid": tag_id
            }
        }

        r = self.send_api(req)
        return r.json()

    # 更新标签
    def update_lable(self, tag_id, tag_upd_name):
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json": {
                "tagid": tag_id,
                "tagname": tag_upd_name
            }
        }

        r = self.send_api(req)
        return r.json()

    # 删除标签
    def delete_lable(self, tag_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}",
        }
        r = self.send_api(req)
        return r.json()

    # 获取标签
    def get_lable(self, tag_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}",
        }
        r = self.send_api(req)
        return r.json()
