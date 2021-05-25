from faker import Faker


class Contact:

    def __init__(self):
        self.fake = Faker('zh_CN')

    def get_name(self):
        return self.fake.name()

    def get_phone(self):
        return self.fake.phone_number()
