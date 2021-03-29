# 测试类
import allure


@allure.feature("计算器功能测试")
class TestCal:

    # 测试相加功能
    @allure.story("相加功能")
    def test_add(self, get_calc, get_add_datas):
        assert round(get_calc.add(get_add_datas[0], get_add_datas[1])) == get_add_datas[2]

    # 测试相减功能
    @allure.story("相减功能")
    def test_sub(self, get_calc, get_sub_datas):
        assert get_calc.sub(get_sub_datas[0], get_sub_datas[1]) == get_sub_datas[2]

    # 测试相乘功能
    @allure.story("相乘功能")
    def test_mul(self, get_calc, get_mul_datas):
        assert get_calc.mul(get_mul_datas[0], get_mul_datas[1]) == get_mul_datas[2]

    # 测试相除功能
    @allure.story("相除功能")
    def test_div(self, get_calc, get_div_datas):
        try:
            assert get_calc.div(get_div_datas[0], get_div_datas[1]) == get_div_datas[2]
        except ZeroDivisionError:
            print("除数不能为0")
