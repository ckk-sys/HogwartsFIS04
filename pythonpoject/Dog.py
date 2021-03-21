from pythonpoject.Animal import Animal


class Dog(Animal):
    # 毛发的属性
    hair = "长毛"

    def __init__(self, name,color,age,gender,hair):
        super(Dog,self).__init__(name,color,age,gender)
        self.hair = hair

    # 狗看家的方法
    def caretaker(self):
        print(f"姓名：{self.name},年龄：{self.age}，性别：{self.gender},毛发：{self.hair},会看家")

    def call(self):
        print(f"{self.name}会汪汪叫")