

import money

#发工资
def send_money():
    print(f"发工资了:发了{1000}")
    money.saved_money += 1000
    # print(id(money.saved_money))