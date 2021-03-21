from pythonpoject.Animal import Animal
from pythonpoject.Cat import Cat
from pythonpoject.Dog import Dog
import yaml

if __name__ == '__main__':
    with open("../datas/cat.yaml",encoding="utf-8") as f:
        cats = yaml.safe_load(f)
    catdate = cats[0]
    cat1=Cat(catdate[0],catdate[1],catdate[2],catdate[3],catdate[4])
    cat1.catch()

    with open("../datas/dog.yaml",encoding="utf-8") as f:
        dogs = yaml.safe_load(f)
    # print(dogs)
    dogdate = dogs["dog1"][0]
    # print(dogdate)
    dog1=Dog(dogdate["name"],dogdate["color"],dogdate["age"],dogdate["gender"],dogdate["hair"])
    dog1.caretaker()