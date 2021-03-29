import allure
import pytest
import yaml

from calculator import Calculator


# 用例名称为中文解析
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture()
def get_calc():
    print("准备开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")


def get_datas():
    with open("./datas/calc.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


def get_adddata():
    data_add = get_datas()['datas']['data_add']
    ids_add = get_datas()['ids']['ids_add']
    return data_add, ids_add


@pytest.fixture(params=get_adddata()[0], ids=get_adddata()[1])
def get_add_datas(request):
    return request.param


def get_subdata():
    data_sub = get_datas()['datas']['data_sub']
    ids_sub = get_datas()['ids']['ids_sub']
    return data_sub, ids_sub


@pytest.fixture(params=get_subdata()[0], ids=get_subdata()[1])
def get_sub_datas(request):
    return request.param


def get_muldata():
    data_mul = get_datas()['datas']['data_mul']
    ids_mul = get_datas()['ids']['ids_mul']
    return data_mul, ids_mul


@pytest.fixture(params=get_muldata()[0], ids=get_muldata()[1])
def get_mul_datas(request):
    return request.param


def get_divdata():
    data_div = get_datas()['datas']['data_div']
    ids_div = get_datas()['ids']['ids_div']
    return data_div, ids_div


@pytest.fixture(params=get_divdata()[0], ids=get_divdata()[1])
def get_div_datas(request):
    return request.param
