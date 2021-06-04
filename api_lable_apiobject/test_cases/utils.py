import yaml
from jsonpath import jsonpath


class Utils:

    @classmethod
    def open_file_load(cls, filename):
        with open(filename, "r", encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def base_jsonpath(cls, obj, json_expr):
        '''
        封装 jsonpath 断言
        :param obj: 要断言的响应内容
        :param json_expr: jsonpath 表达式
        :return: 提取内容的列表
        '''
        return jsonpath(obj, json_expr)
