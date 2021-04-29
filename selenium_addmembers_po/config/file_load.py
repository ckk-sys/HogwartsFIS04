# 读取文件
import yaml


def open_file_load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas
