from pythonpoject.Animal import Animal


class Cat(Animal):

    #毛发的属性
    hair = "短毛"

    def __init__(self,name,color,age,gender,hair):
        super(Cat,self).__init__(name,color,age,gender)
        self.hair = hair

    #捉老鼠的方法
    def catch(self):
        print(f"姓名：{self.name},年龄：{self.age}，性别：{self.gender},毛发：{self.hair},捉老鼠")

    def call(self):
        print(f"{self.name}会喵喵叫")
