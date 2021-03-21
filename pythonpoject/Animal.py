

class Animal:

    name:str
    color:str
    age:int
    gender:str

    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print("会叫")
    def run(self):
        print("会跑")