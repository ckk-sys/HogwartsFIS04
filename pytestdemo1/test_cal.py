
import pytest
from calculator import Calculator


# 测试类
class TestCal:

    def setup_method(self):
        print("准备开始计算")
    def teardown_method(self):
        print("计算结束")

    # 测试相加功能
    data_add=[(1,2,3),(-0.5,-0.2,-0.3),(3,0,3)]
    ids_add=[f"{i}" for i in range(len(data_add))]
    @pytest.mark.parametrize("a,b,expect",data_add,ids=ids_add)
    def test_add(self,a,b,expect):
        calc = Calculator()
        assert calc.add(a, b) == expect

    #测试相减功能
    data_sub=[[10,9,1],[-5,-6,-11],[0.1,0.6,0.6],[0,-0.1,0.1]]
    ids_sub=["正数","负数","小数","正数"]
    @pytest.mark.parametrize("a,b,expect",data_sub,ids=ids_sub)
    def test_sub(self,a,b,expect):
        calc = Calculator()
        assert calc.sub(a, b) == expect

    # 测试相乘功能
    data_mul = [(1, 2, 3), (-0.5, -0.2, -0.3), (3, 0, 3)]
    @pytest.mark.parametrize("a,b,expect", data_mul)
    def test_mul(self,a,b,expect):
        calc = Calculator()
        assert calc.mul(a, b) == expect

    # 测试相除功能
    data_div = [(1, 2, 3), (-0.5, 0, 6), (-6, -2, 3)]
    ids_div = ["分母为正","分母为0","分母为负"]
    @pytest.mark.parametrize("a,b,expect", data_div, ids=ids_div)
    def test_div(self,a,b,expect):
        calc = Calculator()
        assert calc.div(a, b) == expect